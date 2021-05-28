from django.contrib import admin
from .models import EconomyLevel, Resource, Galaxy, FaunaBait, Ingredient

class EconomyLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level')
    list_display_links = ('id', 'name')
    list_per_page = 25

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 25

class GalaxyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'order')
    list_display_links = ('id', 'name')
    list_per_page = 25

class FaunaBaitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 25

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 25

admin.site.register(EconomyLevel, EconomyLevelAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Galaxy, GalaxyAdmin)
admin.site.register(FaunaBait, FaunaBaitAdmin)
admin.site.register(Ingredient, IngredientAdmin)
