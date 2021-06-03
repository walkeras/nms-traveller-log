from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
import logging
from .models import World, Fauna
from bases.models import Base
from reference.models import Resource, Galaxy
from django.db.models import Q, F
from main.views import getGameSession

# Number of Worlds to display per page
WORLDS_PER_PAGE = 10

# Maximum number of paginator page buttons to display
PAGER_WINDOW_SIZE = 15

logger = logging.getLogger(__name__)

isSearch = False


#
# Worlds list page (worlds.html)
# Also used to display search results
#
def index(request):

    global isSearch

    # Get Game Session
    gameSession = getGameSession(request)

    if (request.method == 'GET'):
        isSearch = False

        # Get initial query set ordered by name
        worlds = World.objects.order_by('name')

        # Filter by Game Session
        worlds = worlds.filter(system__game_session__id=gameSession.id)

        total_worlds = len(worlds)

        # Filter by search request parameters
        worlds = evalaute_filters(request, worlds)

        # Only paginate a full World listing (not a Search result)
        if not isSearch:
            # Paginate list
            paginator = Paginator(worlds, WORLDS_PER_PAGE)
            if 'page' in request.GET:
                page = request.GET.get('page')
            else:
                page = 1
            paged_worlds = paginator.get_page(page)

            num_pages = paged_worlds.paginator.num_pages
            logger.debug(f'page {page} of {num_pages}')

            # Determine page number of first pager button
            pager_start = 1
            pager_start_ellipsis = False
            if int(page) > 1 and num_pages > PAGER_WINDOW_SIZE:
                pager_start_ellipsis = True
                pager_start = int(page)
                if pager_start > 1 + num_pages - PAGER_WINDOW_SIZE:
                    pager_start = 1 + num_pages - PAGER_WINDOW_SIZE
            logger.debug(f'pager_start={pager_start}')

            # Determine page number of last pager button
            pager_end = num_pages
            pager_end_ellipsis = False
            if num_pages - int(page) >= PAGER_WINDOW_SIZE:
                pager_end_ellipsis = True
                pager_end = pager_start + PAGER_WINDOW_SIZE - 1
            logger.debug(f'pager_end={pager_end}')

        else:
            # Search results are not paginated
            paged_worlds = worlds
            total_worlds = len(worlds)
            num_pages = 0
            pager_start = 1
            pager_end = 1
            pager_start_ellipsis = False
            pager_end_ellipsis = False

        context = {
            'worlds': paged_worlds,
            'is_search': isSearch,
            'num_pages': num_pages,
            'pager_start': pager_start,
            'pager_start_ellipsis': pager_start_ellipsis,
            'pager_end': pager_end,
            'pager_end_ellipsis': pager_end_ellipsis,
            'pager_range': range(pager_start,pager_end + 1),
            'total_worlds': total_worlds,
            'gameSession': gameSession
        }

    elif (request.method == 'POST'):
        # Quick Name Search
        # Get initial list of Worlds
        worlds = World.objects.order_by('name')

        # Filter by Game Session
        worlds = worlds.filter(system__game_session__id=gameSession.id)

        # Filter list by worldname search parameter
        keywords = request.POST['worldname']
        worlds = worlds.filter(name__icontains=keywords)
        total_worlds = len(worlds)

        context = {
            'worlds': worlds,
            'is_search': True,
            'total_worlds': total_worlds,
            'gameSession': gameSession
        }

    return render(request, 'worlds/worlds.html', context)


#
# Search page for Worlds (search.html)
#
def search(request):
    # Get Game Session
    gameSession = getGameSession(request)

    # Fetch list of Resources from db
    resource_choices = Resource.objects.order_by('name')

    # Prepare list of Galaxies
    galaxy_choices_dict = {}
    for galaxy in list(Galaxy.objects.order_by('name').values()):
        galaxy_choices_dict[galaxy['name']] = galaxy['name']

    context = {
        'resource_choices': resource_choices,
        'weather_hazard_type_choices': World.WEATHER_HAZARD_CHOICES_DICT,
        'fauna_hazard_choices': World.H_M_L_U_CHOICES_DICT,
        'sentinel_hazard_choices': World.H_M_L_U_CHOICES_DICT,
        'galaxy_choices': galaxy_choices_dict,
        'gameSession': gameSession
    }

    return render(request, 'worlds/search.html', context)


#
# Individual World page (world.html)
#
def world(request, world_id):
    # Get Game Session
    gameSession = getGameSession(request)

    # Get requested World
    world = get_object_or_404(World, pk=world_id)

    # Get all Bases on this World
    bases = Base.objects.all().filter(world__pk=world_id)
    for b in bases:
        b.description = b.description.replace("|", ". ")

    # Get all Fauna for this World
    fauna = Fauna.objects.all().filter(world__pk=world_id)

    # Get previous and next world's ordered by name
    qs = World.objects.order_by('name')
    # Next
    next_world = qs.filter(name__gt=world.name).order_by('name').first()
    if next_world is None:
        logger.debug('No next world')
    # Previous
    prev_world = qs.filter(name__lt=world.name).order_by('-name').first()
    if prev_world is None:
        logger.debug('No previous world')

    # Create a list of comments delimited by pipe '|'
    comment_list = world.resources_notes.strip().split('|')

    # Remove potential empty comment at end of list produced by split
    if len(comment_list) > 0 and len(comment_list[len(comment_list) - 1]) == 0:
        del(comment_list[len(comment_list) - 1])

    context = {
        'world': world,
        'prev_world': prev_world,
        'next_world': next_world,
        'bases': bases,
        'comment_list': comment_list,
        'fauna': fauna,
        'gameSession': gameSession
    }

    return render(request, 'worlds/world.html', context)


def evalaute_filters(request, worlds):
    global isSearch

    # If we have search parameters we are coming from the Search page
    # Filter by Description
    if 'description' in request.GET and len(request.GET['description']) > 0:
        isSearch = True
        worlds = worlds.filter(description__icontains=request.GET['description'])

    # Filter by Resource Notes
    if 'resources_notes' in request.GET and len(request.GET['resources_notes']) > 0:
        isSearch = True
        worlds = worlds.filter(resources_notes__icontains=request.GET['resources_notes'])

    # Filter by Resource
    if 'resource' in request.GET and len(request.GET['resource']) > 0:
        resource = request.GET['resource']
        isSearch = True
        # Must use Q filter objects for OR operations
        worlds = worlds.filter(Q(resource_1__name__exact=resource) | Q(resource_2__name__exact=resource) | Q(resource_3__name__exact=resource) | Q(resource_4__name__exact=resource) | Q(resource_5__name__exact=resource) | Q(resource_6__name__exact=resource))

    # Filter by Weather
    if 'weather' in request.GET and len(request.GET['weather']) > 0:
        isSearch = True
        worlds = worlds.filter(weather_hazard_type__exact=request.GET['weather'])

    # Filter by Exotic
    if 'exotic' in request.GET and len(request.GET['exotic']) > 0:
        isSearch = True
        worlds = worlds.filter(is_exotic__exact=(request.GET['exotic'] == 'True'))

    # Filter by Weather Notes
    if 'weather_notes' in request.GET and len(request.GET['weather_notes']) > 0:
        isSearch = True
        worlds = worlds.filter(weather_notes__icontains=request.GET['weather_notes'])

    # Filter by Weather Description
    if 'weather_desc' in request.GET and len(request.GET['weather_desc']) > 0:
        isSearch = True
        worlds = worlds.filter(weather_desc__icontains=request.GET['weather_desc'])

    # Filter by Fauna Hazard Level
    if 'fauna_hazard' in request.GET and len(request.GET['fauna_hazard']) > 0:
        isSearch = True
        worlds = worlds.filter(fauna_hostility_level__exact=request.GET['fauna_hazard'])

    # Filter by Sentinel Hostility Level
    if 'sentinel_hazard' in request.GET and len(request.GET['sentinel_hazard']) > 0:
        isSearch = True
        worlds = worlds.filter(sentinel_hostility_level__exact=request.GET['sentinel_hazard'])

    # Filter by Extreme
    if 'extreme' in request.GET and len(request.GET['extreme']) > 0:
        isSearch = True
        worlds = worlds.filter(is_weather_extreme__exact=(request.GET['extreme'] == 'True'))

    # Filter by Favourite
    if 'favourite' in request.GET and len(request.GET['favourite']) > 0:
        isSearch = True
        worlds = worlds.filter(favourite__exact=(request.GET['favourite'] == 'True'))

    # Filter by Portal Address
    if 'portal_address' in request.GET and len(request.GET['portal_address']) > 0:
        isSearch = True
        worlds = worlds.filter(portal_address__iexact=request.GET['portal_address'])

    # Filter by Galaxy
    if 'galaxy' in request.GET and len(request.GET['galaxy']) > 0:
        isSearch = True
        worlds = worlds.filter(system__galaxy__name__exact=request.GET['galaxy'])

    # Filter by All Fauna Found
    if 'all_fauna_found' in request.GET and request.GET['all_fauna_found'] == 'on':
        isSearch = True
        worlds = worlds.filter(fauna_discovered__exact=F('fauna_maximum'), fauna_maximum__gt=0)

    return worlds
