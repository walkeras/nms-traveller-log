from django.contrib import admin
from .models import Gallery
from systems.models import System
from worlds.models import World

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'type')
    list_display_links = ('id', 'description')
    list_per_page = 25

    # Sort choices in FK dropdowns
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "system":
            kwargs["queryset"] = System.objects.order_by('name')
        elif db_field.name == "world":
            kwargs["queryset"] = World.objects.order_by('name')

        return super(GalleryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Gallery, GalleryAdmin)
