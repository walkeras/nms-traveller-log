from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import logging
from .models import Base
from main.models import GameSession
from main.views import getGameSession

logger = logging.getLogger(__name__)

def index(request):
    bases = Base.objects.order_by('name')

    # Get Game Session
    gameSession = getGameSession(request)

    # Filter by Game Session
    bases = bases.filter(world__system__game_session__id=gameSession.id)
    total_bases = len(bases)

    paginator = Paginator(bases, 10)
    page = request.GET.get('page')
    paged_bases = paginator.get_page(page)

    for b in paged_bases:
        b.description = b.description.replace("|", " - ")

    context = {
        'bases': paged_bases,
        'gameSession': gameSession,
        'total_bases': total_bases
    }

    return render(request, 'bases/bases.html', context)

def base(request, base_id):

    # Get Game Session
    gameSession = getGameSession(request)

    # Get requested Base
    base = get_object_or_404(Base, pk=base_id)

    # Get previous and next Base ordered by name
    qs = Base.objects.order_by('name')
    # Next
    next_base = qs.filter(name__gt=base.name).order_by('name').first()
    if next_base == None:
        logger.debug('No next base')
    # Previous
    prev_base = qs.filter(name__lt=base.name).order_by('-name').first()
    if prev_base == None:
        logger.debug('No previous base')

    # Create a list of comments delimited by pipe '|'
    comment_list = base.description.strip().split('|')
    base.description = base.description.replace("|", " - ")

    context = {
        'base': base,
        'prev_base': prev_base,
        'next_base': next_base,
        'comment_list': comment_list,
        'gameSession': gameSession
    }

    return render(request, 'bases/base.html', context)
