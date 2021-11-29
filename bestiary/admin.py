from django.contrib import admin
from .models import Monster

# Register your models here.


class MonsterAdmin(admin.ModelAdmin):
    search_fields = ["name", "AL"]
    list_display = ["name", "HD", "AL"]
    list_filter = ["AL"]


admin.site.register(Monster, MonsterAdmin)
