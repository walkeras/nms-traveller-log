from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import logging
from .models import Gallery

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    items = Gallery.objects.order_by("-id")
    categories = []

    if 'category' in request.GET and len(request.GET['category']) > 0:
        logger.debug(request.GET['category'])
        categories = request.GET['category'].strip().split()
        logger.debug(categories)

        if 'ruin' in categories:
            logger.debug("Include Ruins")
        else:
            items = items.exclude(type__exact=Gallery.ANCIENT_RUIN)

        if 'monolith' in categories:
            logger.debug("Include Monoliths")
        else:
            items = items.exclude(type__exact=Gallery.ALIEN_MONOLITH)

        if 'anomaly' in categories:
            logger.debug("Include Anomalies")
        else:
            items = items.exclude(type__exact=Gallery.SPACE_ANOMALY)

        if 'fauna' in categories:
            logger.debug("Include Fauna")
        else:
            items = items.exclude(type__exact=Gallery.FAUNA)

        if 'misc' in categories:
            logger.debug("Include Miscellaneous")
        else:
            items = items.exclude(type__exact=Gallery.MISCELLANEOUS)

        if 'landscape' in categories:
            logger.debug("Include Landscape")
        else:
            items = items.exclude(type__exact=Gallery.LANDSCAPE)

        if 'flora' in categories:
            logger.debug("Include Flora")
        else:
            items = items.exclude(type__exact=Gallery.FLORA)

    paginator = Paginator(items, 12)
    page = request.GET.get('page')
    paged_items = paginator.get_page(page)

    context = {
        'gallery' : paged_items,
        'categories': categories
    }

    return render(request, 'gallery/gallery.html', context)
