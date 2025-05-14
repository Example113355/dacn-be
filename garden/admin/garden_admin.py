from django.contrib import admin


class GardenAdmin(admin.ModelAdmin):
    list_display = ("id", 'item', 'status')