from django.contrib import admin

from planetas.models import Planeta

@admin.register(Planeta)
class PlanetaAdmin(admin.ModelAdmin):
    list_display = ("name", "diameter", "created", "updated")
