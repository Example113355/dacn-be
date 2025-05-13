from django.urls import path
from inventory.views import InventoryView

urlpatterns = [
    path('', InventoryView.as_view({'get': 'list'}), name='inventory-list'),
]
