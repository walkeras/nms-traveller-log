from django.contrib import admin
from .models import System
from reference.models import EconomyLevel


class SystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'discovered_date', 'economy_level', 'race', 'portal_address', 'near_system', 'gc_dist')
    list_display_links = ('id', 'name')
    list_per_page = 25

    # Sort choices in FK dropdowns
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "economy_level":
            kwargs["queryset"] = EconomyLevel.objects.order_by('name')
        elif db_field.name == "near_system" or db_field.name == "black_hole_dest_system":
            kwargs["queryset"] = System.objects.order_by('name')

        return super(SystemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(System, SystemAdmin)
