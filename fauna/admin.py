from django.contrib import admin
from .models import World, Fauna
from reference.models import FaunaBait, Ingredient


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


admin.site.register(Fauna, FaunaAdmin)
