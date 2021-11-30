from django.contrib import admin
from django.contrib.admin.helpers import InlineAdminForm

from .models import Territory, Location, Rumor

# Register your models here.


class RumorInline(admin.TabularInline):
    model = Rumor
    extra = 2


class LocationAdmin(admin.ModelAdmin):
    inlines = [RumorInline]
    list_display = ("name", "territory")


class LocationInline(admin.TabularInline):
    model = Location
    extra = 5


class TerritoryAdmin(admin.ModelAdmin):
    inlines = [LocationInline]


admin.site.register(Territory, TerritoryAdmin)
admin.site.register(Location, LocationAdmin)
