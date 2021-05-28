from django.contrib import admin
from .models import Base
from worlds.models import World
from reference.models import Galaxy

class BaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'world')
    list_display_links = ('id', 'name')
    list_per_page = 25

    # Sort choices in FK dropdowns
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "world":
            kwargs["queryset"] = World.objects.order_by('name')
        elif db_field.name == "galaxy":
            kwargs["queryset"] = Galaxy.objects.order_by('name')

        return super(BaseAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Base, BaseAdmin)
