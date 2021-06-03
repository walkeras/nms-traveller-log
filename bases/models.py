from django.db import models
from worlds.models import World
from reference.models import Galaxy


class Base(models.Model):
    """
    Base.

    May have multiple Bases per World.
    """

    # Name
    name = models.CharField(max_length=50, blank=False, unique=True)

    # Description
    description = models.TextField(blank=True, help_text="Use the pipe '|' character to list multiple items")

    # Galaxy
    galaxy = models.ForeignKey(Galaxy, null=True, on_delete=models.DO_NOTHING, default=1)

    # Photos
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    # Portal Address
    portal_address = models.CharField(max_length=200, blank=True)

    # Each base is on one World
    world = models.ForeignKey(World, blank=True, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name
