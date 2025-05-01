from django.contrib import admin
from item.models.item_model import Item
from item.admin.item_admin import ItemAdmin

admin.site.register(Item, ItemAdmin)