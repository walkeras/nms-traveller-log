import re
from django.contrib import admin
from .models import World, Fauna
from reference.models import Resource, FaunaBait, Ingredient
from systems.models import System


class WorldAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'has_base', 'is_exotic', 'system')
    list_display_links = ('id', 'name')
    list_per_page = 25

    # Sort choices in FK dropdowns
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if re.match(r"resource_[0-9]", db_field.name):
            kwargs["queryset"] = Resource.objects.order_by('name')
        elif db_field.name == "system":
            kwargs["queryset"] = System.objects.order_by('name')

        return super(WorldAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class FaunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'world')
    list_display_links = ('id', 'name', 'world')
    list_per_page = 25

    # Sort choices in FK dropdowns
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "bait":
            kwargs["queryset"] = FaunaBait.objects.order_by('name')
        elif db_field.name == "flesh":
            kwargs["queryset"] = Ingredient.objects.order_by('name')
        elif db_field.name == "product":
            kwargs["queryset"] = Ingredient.objects.order_by('name')
        elif db_field.name == "world":
            kwargs["queryset"] = World.objects.order_by('name')

        return super(FaunaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(World, WorldAdmin)
admin.site.register(Fauna, FaunaAdmin)
