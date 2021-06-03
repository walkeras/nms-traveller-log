from django.db import models


#
# Model to hold Game Sessions
#
class GameSession(models.Model):

    XBOX = 'XBox'
    STEAM = 'Steam'
    PLAYSTATION = 'PlayStation'
    WINDOWS = 'Windows'

    PLATFORM_CHOICES = [(XBOX, XBOX), (STEAM, STEAM), (PLAYSTATION, PLAYSTATION), (WINDOWS, WINDOWS)]
    PLATFORM_CHOICES_DICT = dict(PLATFORM_CHOICES)

    SURVIVAL = "Survival"
    CREATIVE = "Creative"
    NORMAL = "Normal"
    PERMADEATH = "Perma-Death"

    SESSION_TYPE_CHOICES = [(SURVIVAL, SURVIVAL), (CREATIVE, CREATIVE), (NORMAL, NORMAL), (PERMADEATH, PERMADEATH)]
    SESSION_TYPE_CHOICES_DICT = dict(SESSION_TYPE_CHOICES)

    # Name
    name = models.CharField(max_length=50, blank=False, null=False)

    # Platform
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, blank=True, null=True)

    # Session Type
    session_type = models.CharField(max_length=20, choices=SESSION_TYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
