import logging
from datetime import datetime
from django.db import models
from reference.models import EconomyLevel, Galaxy
from main.models import GameSession

logger = logging.getLogger(__name__)


class System(models.Model):
    STAR_COLOUR_CHOICES = [('Yellow', 'Yellow'), ('Red', 'Red'), ('Green', 'Green'), ('Blue', 'Blue'), ('Unknown', 'Unknown')]
    STAR_COLOUR_CHOICES_DICT = dict(STAR_COLOUR_CHOICES)

    RACE_CHOICES = [('Gek', 'Gek'), ('Korvax', 'Korvax'), ('Vykeen', 'Vykeen'), ('Uncharted', 'Uncharted')]
    RACE_CHOICES_DICT = dict(RACE_CHOICES)

    SPACE_STATION_CHOICES = [('Y', 'Present'), ('N', 'None'), ('A', 'Abandoned')]
    SPACE_STATION_CHOICES_DICT = dict(SPACE_STATION_CHOICES)

    # System Name
    name = models.CharField(max_length=50, unique=True)

    # Black Hole
    black_hole = models.BooleanField(blank=False, default=False, help_text="Black Hole present in this system")

    # Black Hole Destination System
    black_hole_dest_system = models.ForeignKey('self', blank=True, null=True, on_delete=models.DO_NOTHING, related_name="black_hole_dest_system_link")

    # Comments
    comments = models.TextField(blank=True, help_text="Use the pipe '|' character to list multiple items")

    # Conflict Level
    conflict_level = models.CharField(max_length=20, blank=True)

    # Derelict Freighter Name
    derelict_freighter_name = models.CharField(max_length=50, blank=True)

    # Derelict Freighter Notes
    derelict_freighter_notes = models.TextField(blank=True)

    # Discovered date
    discovered_date = models.DateTimeField(default=datetime.now, blank=True)

    # Discovered By
    discovered_by_me = models.BooleanField(blank=False, default=True)

    # Economy Description - Metallurgic, Scientific, Manufacturing, etc
    economy_desc = models.CharField(max_length=30, blank=True)

    # Economy Level
    economy_level = models.ForeignKey(EconomyLevel, on_delete=models.DO_NOTHING)

    # Galaxy
    galaxy = models.ForeignKey(Galaxy, null=True, on_delete=models.DO_NOTHING, default=1)

    # Game Session
    game_session = models.ForeignKey(GameSession, null=False, on_delete=models.DO_NOTHING, default=1)

    # Distance to Galactic Center (LY)
    gc_dist = models.IntegerField(blank=True, null=True)

    # Nearest system and distance
    near_system = models.ForeignKey('self', blank=True, null=True, on_delete=models.DO_NOTHING)
    near_system_dist = models.IntegerField(blank=True, null=True)

    # Number of Moons
    num_moons = models.IntegerField(blank=True, null=True)

    # Number of Planets
    num_planets = models.IntegerField(blank=True, null=True)

    # Photos
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    # Portal Address
    portal_address = models.CharField(max_length=200, blank=True, help_text="Hex code from https://nmsportals.github.io/")

    # Race
    race = models.CharField(max_length=9, choices=RACE_CHOICES)

    # Region
    region = models.CharField(max_length=50, blank=True)

    # Space Station
    space_station = models.CharField(max_length=1, blank=True, choices=SPACE_STATION_CHOICES)

    # Star Classification
    star_classification = models.CharField(max_length=5, blank=True)

    # Star Colour - Red/Blue/Green/Yellow/Unknown
    star_colour = models.CharField(max_length=7, blank=True, choices=STAR_COLOUR_CHOICES, default='Unknown')

    # Number of Stars: 1 - Single Star, 2 - Binary System, 3 - Trinary System
    star_count = models.IntegerField(blank=False, default=1)

    # Teleportable
    teleportable = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.name

    @property
    def photo_main_url(self):
        if self.photo_main and hasattr(self.photo_main, 'url'):
            return self.photo_main.url

        return "/static/img/default_system_image.png"
