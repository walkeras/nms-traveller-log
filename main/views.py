from django.shortcuts import render
import logging
from .models import GameSession

logger = logging.getLogger(__name__)


def index(request):
    items = GameSession.objects.order_by("id")

    # Get existing Game Session
    gameSession = getGameSession(request)

    context = {
        'gamesessions': items,
        'gameSession': gameSession
    }

    return render(request, 'gamesessions/gamesession.html', context)


def getGameSession(request):
    # Get Game Session information from cookie "game_session"
    gameSessionId = request.COOKIES.get("game_session")
    if gameSessionId and len(gameSessionId) > 0:
        logger.debug("Cookie game_session=" + request.COOKIES.get("game_session"))
        logger.debug("Cookie game_session=" + request.COOKIES.get("game_session"))
        gameSession = GameSession.objects.get(pk=gameSessionId)
        logger.debug("Game Session: " + gameSession.name + ", " + gameSession.platform + ", " + str(gameSession.id))
        return gameSession
    else:
        gameSession = GameSession.objects.order_by("id").first()
        logger.debug("Defaulting Game Session: " + gameSession.name + ", " + gameSession.platform + ", " + str(gameSession.id))
        return gameSession
