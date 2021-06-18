from django.shortcuts import render
from django.core.paginator import Paginator
import logging
from .models import Fauna
from main.views import getGameSession

sortByChoices = {'byEntryOrder': 'Entry Order', 'byName': 'Name', 'byWorld': 'World'}

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):

    # Get Game Session
    gameSession = getGameSession(request)

    if (request.method == 'GET'):

        sortBy = ''
        if 'sortBy' in request.GET:
            if (request.GET['sortBy'] == 'byName'):
                logger.debug('Sort By Name')
                sortBy = 'byName'
                fauna = Fauna.objects.order_by("name")
            elif (request.GET['sortBy'] == 'byEntryOrder'):
                logger.debug('Sort By Entry Order')
                sortBy = 'byEntryOrder'
                fauna = Fauna.objects.order_by('-id')
            elif (request.GET['sortBy'] == 'byWorld'):
                logger.debug('Sort By World')
                sortBy = 'byWorld'
                fauna = Fauna.objects.order_by('world__name')
            else:
                # Default sort order: Most recently entered first
                fauna = Fauna.objects.order_by("-id")
        else:
            # Default sort order: Most recently entered first
            fauna = Fauna.objects.order_by('-id')

        # Filter by Game Session
        fauna = fauna.filter(world__system__game_session__id=gameSession.id)

        paginator = Paginator(fauna, 12)
        page = request.GET.get('page')
        paged_items = paginator.get_page(page)

        context = {
            'fauna': paged_items,
            'total_fauna': len(fauna),
            'sortByChoices': sortByChoices,
            'sortBy': sortBy,
            'gameSession': gameSession
        }

    return render(request, 'fauna/fauna.html', context)
