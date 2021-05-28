from django.db import models
from reference.models import Resource, FaunaBait, Ingredient
from systems.models import System

'''
    World
'''
class World(models.Model):

    # High/Medium/Low/Unknown Choices
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    UNKNOWN = 'U'
    H_M_L_U_CHOICES = [(HIGH, 'High'), (MEDIUM, 'Medium'), (LOW, 'Low'), (UNKNOWN, 'Unknown')]
    H_M_L_U_CHOICES_DICT = dict(H_M_L_U_CHOICES)

    # Planet/Moon Choices
    PLANET = 'PLANET'
    MOON = 'MOON'
    PLANET_MOON_CHOICES = [(PLANET, 'Planet'), (MOON, 'Moon')]

    # Weather Hazard Choices
    NONE = 'N'
    HEAT = 'H'
    COLD = 'C'
    TOXIC = 'T'
    RADIATION = 'R'
    HOT_RAIN = 'S'
    WEATHER_HAZARD_CHOICES = [(NONE, 'None'),(HEAT, 'Heat'),(HOT_RAIN, 'Hot Rain'),(COLD, 'Cold'),(TOXIC, 'Toxic'),(RADIATION, 'Radiation'),(UNKNOWN, 'Unknown')]
    WEATHER_HAZARD_CHOICES_DICT = dict(WEATHER_HAZARD_CHOICES)

    # Name
    name = models.CharField(max_length=50, unique=True, blank=False)

    # Description - eg. Tropical Planet
    description = models.CharField(max_length=50, blank=True, help_text="From Starship Scan")

    # Fauna Description - eg. Bountiful, etc
    fauna_desc = models.CharField(max_length=20, blank=True, help_text="From Discovery Data")

    # Fauna Discovered
    fauna_discovered = models.IntegerField(blank=True, null=True);

    # Fauna Hostility Description - eg. No Attacks, Frequent Attacks, Occasional Attacks
    fauna_hostility_desc = models.CharField(max_length=50, blank=True, help_text="Additional description, eg. Frequent Attacks, Occasional Attacks")

    # Fauna Hostility Level - H/M/L/U
    fauna_hostility_level = models.CharField(max_length=1, default=UNKNOWN, choices=H_M_L_U_CHOICES, help_text="Low - No attacks. Medium - Occasional Attacks. High - Frequent Attacks.")

    # Fauna Maximum
    fauna_maximum = models.IntegerField(blank=True, null=True);

    # Favourite
    favourite = models.BooleanField(default=False);

    # Flora Description - eg. Bountiful, etc
    flora_desc = models.CharField(max_length=20, blank=True, help_text="From Discovery Data")

    # Base?
    has_base = models.BooleanField(default=False)

    # Exotic?
    is_exotic = models.BooleanField(default=False)

    # Extreme Weather?
    is_weather_extreme = models.BooleanField(default=False)

    # Photos
    photo_marquee = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    # Portal Address
    portal_address = models.CharField(max_length=200, blank=True, help_text="Hex code from https://nmsportals.github.io/")

    # Resources
    resource_1 = models.ForeignKey(Resource, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='resource_1')
    resource_2 = models.ForeignKey(Resource, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='resource_2')
    resource_3 = models.ForeignKey(Resource, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='resource_3')
    resource_4 = models.ForeignKey(Resource, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='resource_4')
    resource_5 = models.ForeignKey(Resource, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='resource_5')
    resource_6 = models.ForeignKey(Resource, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='resource_6')

    # Resource Notes
    resources_notes = models.TextField(blank=True, help_text="Additional notes, eg. Ancient Bones, Tech Modules, resource occurrence frequency. Use the pipe '|' character to list multiple items.")

    # Setinel Description - eg. Aggressive, High Activity, etc
    sentinel_desc = models.CharField(max_length=30, blank=True, help_text="From Discovery Data")

    # Sentinel Hostility Description - eg. No Attacks, Frequent Attacks, Occasional Attacks
    sentinel_hostility_desc = models.CharField(max_length=50, blank=True, help_text="Additional description, eg. Frequent Attacks, Attack on sight")

    # Sentinel Hostility Level - H/M/L/U
    sentinel_hostility_level = models.CharField(max_length=1, default=UNKNOWN, choices=H_M_L_U_CHOICES, help_text="Low - Normal/Low presence. Medium - Frequent scans/High presence. High - Attack on sight.")

    # System
    system = models.ForeignKey(System, blank=False, on_delete=models.DO_NOTHING)

    # Type - Planet/Moon
    type = models.CharField(max_length=6, default=PLANET, choices=PLANET_MOON_CHOICES)

    # Weather Description
    weather_desc = models.CharField(max_length=50, blank=True, help_text="From Discovery Data")

    # Weather Hazard Type - eg. None/Heat/Cold/Toxic/Radiation/Unknown
    weather_hazard_type = models.CharField(max_length=1, default=UNKNOWN, choices=WEATHER_HAZARD_CHOICES)

    # Weather Notes - eg. Frequent Storms, Occasional Storms
    weather_notes = models.CharField(max_length=50, blank=True, help_text="Additional description, eg. Frequent Storms, Occasional Storms")

    # Weather Rating
    weather_rating = models.CharField(max_length=1, default=UNKNOWN, choices=H_M_L_U_CHOICES, help_text="Low - Day/Night Only hazard with Infrequent Storms. Medium - Constant hazard. High - Frequent Storms or Extreme World.")

    def __str__(self):
        return self.name

'''
    Fauna
'''
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
    world = models.ForeignKey(World, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
