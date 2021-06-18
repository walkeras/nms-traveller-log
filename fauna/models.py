from django.db import models
from reference.models import FaunaBait, Ingredient
from worlds.models import World


#
# Fauna
#
class Fauna(models.Model):

    # Bait
    bait = models.ForeignKey(FaunaBait, null=True, blank=True, on_delete=models.DO_NOTHING)

    # Description
    description = models.CharField(max_length=200, null=True, blank=True, help_text="Additional notes")

    # Flesh
    flesh = models.ForeignKey(Ingredient, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='flesh_ingredient')

    # Is Hostile?
    is_hostile = models.BooleanField(default=False)

    # Name
    name = models.CharField(max_length=50, unique=True, blank=False, help_text="From Discovery Data")

    # Photo
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    # Product
    product = models.ForeignKey(Ingredient, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='product_ingredient')

    # World
    world = models.ForeignKey(World, null=True, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
