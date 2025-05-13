from django.contrib import admin
from inventory.models import Inventory


class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "quantity",
        "item",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at")

admin.site.register(Inventory, InventoryAdmin)
