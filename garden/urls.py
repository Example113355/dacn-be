from django.urls import path
from garden.views.garden_view import GardenView

urlpatterns = [
    path('', GardenView.as_view({"get": "list", "post": "create"}), name='garden-list'),
]