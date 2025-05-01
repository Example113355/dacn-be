from django.contrib import admin
from garden.models.garden_model import Garden
from garden.admin.garden_admin import GardenAdmin

admin.site.register(Garden, GardenAdmin)