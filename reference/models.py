from django.db import models

#
# EconomyLevel
#
class EconomyLevel(models.Model):
    ECONOMY_LEVEL_CHOICES = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('U', 'U'), ('X', 'X')]
    ECONOMY_LEVEL_CHOICES_DICT = {
        'A': 'A - Top Tier',
        'B': 'B - Middle Tier',
        'C': 'C - Bottom Tier',
        'U': 'U - Unknown',
        'X': 'X - No Data'
        }

    # Economy Level Name
    name = models.CharField(max_length=20)

    # Level - A/B/C/U - Unknown/X - Data Unavailable
    level = models.CharField(max_length=1,choices=ECONOMY_LEVEL_CHOICES,default='U')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'],name='unique_level_name'),
        ]

    def __str__(self):
        return self.name

#
# Resource
#
class Resource(models.Model):
    # Resource Name
    name = models.CharField(max_length=50,blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'],name='unique_resource_name'),
        ]

    def __str__(self):
        return self.name

#
# Galaxy
#
class Galaxy(models.Model):
    GALAXY_TYPE_CHOICES = [('Norm', 'Norm'), ('Lush', 'Lush'), ('Harsh', 'Harsh'), ('Empty', 'Empty')]
    GALAXY_TYPE_CHOICES_DICT = {
        'Norm': 'Norm',
        'Lush': 'Lush',
        'Harsh': 'Harsh',
        'Empty': 'Empty'
        }

    # Galaxy Name
    name = models.CharField(max_length=50,blank=False)

    # Galaxy type
    type = models.CharField(max_length=5, choices=GALAXY_TYPE_CHOICES,default='Norm')

    # Galaxy Order
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'],name='unique_galaxy_name'),
        ]

    def __str__(self):
        return self.name

#
# Fauna Bait
#
class FaunaBait(models.Model):
    # Bait Name
    name = models.CharField(max_length=50,blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'],name='unique_faunabait_name'),
        ]

    def __str__(self):
        return self.name

#
# Ingredient
#
class Ingredient(models.Model):
    # Name
    name = models.CharField(max_length=50,blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'],name='unique_ingredient_name'),
        ]

    def __str__(self):
        return self.name
