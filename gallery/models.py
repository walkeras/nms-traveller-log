from django.db import models
from systems.models import System
from worlds.models import World

class Gallery(models.Model):

    ALIEN_MONOLITH = 'Alien Monolith'
    ANCIENT_RUIN = 'Ancient Ruin'
    FAUNA = 'Fauna'
    FLORA = 'Flora'
    LANDSCAPE = 'Landscape'
    MISCELLANEOUS = 'Miscellaneous'
    SPACE_ANOMALY = 'Space Anomaly'

    TYPE_CHOICES = [(ALIEN_MONOLITH, ALIEN_MONOLITH), (ANCIENT_RUIN, ANCIENT_RUIN), (SPACE_ANOMALY, SPACE_ANOMALY), (FAUNA, FAUNA), (FLORA, FLORA), (LANDSCAPE, LANDSCAPE),(MISCELLANEOUS, MISCELLANEOUS)]
    TYPE_CHOICES_DICT = dict(TYPE_CHOICES)

    # Coordinates
    coordinates = models.CharField(max_length=20, null=True, blank=True)

    # Description
    description = models.TextField(blank=True)

    # Photo
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    # System
    system = models.ForeignKey(System, null=True, on_delete=models.DO_NOTHING, blank=True)

    # Type
    type = models.CharField(max_length=30,choices=TYPE_CHOICES)

    # World
    world = models.ForeignKey(World, null=True, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return self.description

