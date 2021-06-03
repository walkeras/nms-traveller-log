from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.db.models import Count, F
import logging
from .models import System
from worlds.models import World
from reference.models import EconomyLevel, Galaxy
from main.views import getGameSession

SYSTEMS_PER_PAGE = 9

sortByChoices = {'byDiscoveryDate': 'Discovery Date', 'byName': 'Name', 'byGCDistance': 'GC Distance'}

logger = logging.getLogger(__name__)

isSearch = False


#
# List of Systems page (systems.html)
#
def index(request):

    global isSearch

    # Get Game Session
    gameSession = getGameSession(request)

    if (request.method == 'GET'):
        isSearch = False

        # TODO: Only full system listing supports sorting - not the Search results
        sortBy = ''
        if 'sortBy' in request.GET:
            if (request.GET['sortBy'] == 'byName'):
                logger.debug('Sort By Name')
                sortBy = 'byName'
                systems = System.objects.order_by('name')
            elif (request.GET['sortBy'] == 'byDiscoveryDate'):
                logger.debug('Sort By Discovery Date')
                sortBy = 'byDiscoveryDate'
                systems = System.objects.order_by('-discovered_date')
            elif (request.GET['sortBy'] == 'byGCDistance'):
                logger.debug('Sort By GC Distance')
                sortBy = 'byGCDistance'
                systems = System.objects.order_by('gc_dist')
            else:
                # Default sort order: Most recently discovered systems first
                systems = System.objects.order_by('-discovered_date')
        else:
            # Default sort order: Most recently discovered systems first
            systems = System.objects.order_by('-discovered_date')

        # Filter by Game Session
        systems = systems.filter(game_session__id=gameSession.id)

        # Filter by search request parameters
        systems = evalaute_filters(request, systems)

        # Only paginate a full System listing (not a Search result)
        if not isSearch:
            paginator = Paginator(systems, SYSTEMS_PER_PAGE)
            page = request.GET.get('page')
            paged_systems = paginator.get_page(page)
        else:
            paged_systems = systems

        systemCount = len(systems)

        context = {
            'systems': paged_systems,
            'is_search': isSearch,
            'sortByChoices': sortByChoices,
            'sortBy': sortBy,
            'systemCount': systemCount,
            'gameSession': gameSession
        }

        return render(request, 'systems/systems.html', context)
    elif (request.method == 'POST'):

        if request.POST['logout']:
            # Logout request
            logger.debug("Logout request received.")
            logout(request)
            return redirect('systems')
        else:
            # Assume this as a Search request
            # Get initial list of Systems
            systems = System.objects.order_by('-discovered_date')

            # Filter by Game Session
            systems = systems.filter(game_session__id=gameSession.id)

            # Filter list by systemname search parameter
            keywords = request.POST['systemname']
            systems = systems.filter(name__icontains=keywords)
            systemCount = len(systems)

            context = {
                'systems': systems,
                'sortByChoices': sortByChoices,
                'systemCount': systemCount,
                'gameSession': gameSession
            }

            return render(request, 'systems/systems.html', context)


#
# Individual System page (system.html)
#
def system(request, system_id):
    # Get Game Session
    gameSession = getGameSession(request)

    # Get requested System
    system = get_object_or_404(System, pk=system_id)

    # Get previous and next system ordered by name
    qs = System.objects.order_by('name')
    # Next
    next_system = qs.filter(name__gt=system.name).order_by('name').first()
    if next_system is None:
        logger.debug('No next system')
    # Previous
    prev_system = qs.filter(name__lt=system.name).order_by('-name').first()
    if prev_system is None:
        logger.debug('No previous system')

    # Get all Worlds linked to this system
    worlds = World.objects.all().filter(system__pk=system_id).order_by('name')

    # Create a list of comments delimited by pipe '|'
    comment_list = system.comments.strip().split('|')

    context = {
        'system': system,
        'prev_system': prev_system,
        'next_system': next_system,
        'worlds': worlds,
        'comment_list': comment_list,
        'gameSession': gameSession
    }

    return render(request, 'systems/system.html', context)


#
# Search page for Systems (search.html)
#
def search(request):
    # Get Game Session
    gameSession = getGameSession(request)

    # Prepare list of Galaxies
    galaxy_choices_dict = {}
    for galaxy in list(Galaxy.objects.order_by('name').values()):
        galaxy_choices_dict[galaxy['name']] = galaxy['name']

    context = {
        'race_choices': System.RACE_CHOICES_DICT,
        'star_colour_choices': System.STAR_COLOUR_CHOICES_DICT,
        'economy_level_choices': EconomyLevel.ECONOMY_LEVEL_CHOICES_DICT,
        'galaxy_choices': galaxy_choices_dict,
        'gameSession': gameSession
    }

    return render(request, 'systems/search.html', context)


#
# Evaluate system search filters
#
def evalaute_filters(request, systems):
    global isSearch
    # If we have search parameters we are coming from the Search page
    # Filter by Comments
    if 'comments' in request.GET and len(request.GET['comments']) > 0:
        isSearch = True
        systems = systems.filter(comments__icontains=request.GET['comments'])

    # Filter by Economy Level
    if 'economy_level' in request.GET and len(request.GET['economy_level']) > 0:
        isSearch = True
        systems = systems.filter(economy_level__level__exact=request.GET['economy_level'])

    # Filter by Star Colour
    if 'star_colour' in request.GET and len(request.GET['star_colour']) > 0:
        isSearch = True
        systems = systems.filter(star_colour__exact=request.GET['star_colour'])

    # Filter by Economy Description
    if 'economy_desc' in request.GET and len(request.GET['economy_desc']) > 0:
        isSearch = True
        systems = systems.filter(economy_desc__icontains=request.GET['economy_desc'])

    # Filter by Race
    if 'race' in request.GET and len(request.GET['race']) > 0:
        isSearch = True
        systems = systems.filter(race__exact=request.GET['race'])

    # Partially Mapped Systems checkbox
    if 'partially_mapped_systems' in request.GET and request.GET['partially_mapped_systems'] == 'on':
        isSearch = True
        # Add virtual field 'num_mapped_worlds' to the result set
        systems = systems.annotate(num_mapped_worlds=Count('world'))
        # Exclude systems from the result set that have all worlds mapped
        systems = systems.exclude(num_mapped_worlds__exact=F('num_planets') + F('num_moons'))

    # Filter by Black Hole
    if 'black_hole' in request.GET and request.GET['black_hole'] == 'on':
        isSearch = True
        systems = systems.filter(black_hole__exact=True)

    # Filter by Galaxy
    if 'galaxy' in request.GET and len(request.GET['galaxy']) > 0:
        isSearch = True
        systems = systems.filter(galaxy__name__exact=request.GET['galaxy'])

    # Filter by Portal Address
    if 'portal_address' in request.GET and len(request.GET['portal_address']) > 0:
        isSearch = True
        systems = systems.filter(portal_address__iexact=request.GET['portal_address'])

    # Derelict Freighter Salvaged checkbox
    if 'derelict_freighter_salvaged' in request.GET and request.GET['derelict_freighter_salvaged'] == 'on':
        isSearch = True
        systems = systems.exclude(derelict_freighter_name__exact='')

    # Derelict Freighter Name
    if 'derelict_freighter_name' in request.GET and len(request.GET['derelict_freighter_name']) > 0:
        isSearch = True
        systems = systems.filter(derelict_freighter_name__icontains=request.GET['derelict_freighter_name'])

    # Derelict Freighter Notes
    if 'derelict_freighter_notes' in request.GET and len(request.GET['derelict_freighter_notes']) > 0:
        isSearch = True
        systems = systems.filter(derelict_freighter_notes__icontains=request.GET['derelict_freighter_notes'])

    return systems
