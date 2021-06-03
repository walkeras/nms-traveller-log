from django.contrib import admin
from .models import GameSession


class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'platform', 'session_type')
    list_display_links = ('id', 'name')
    list_per_page = 25


admin.site.register(GameSession, GameSessionAdmin)
