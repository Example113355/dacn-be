from django.urls import path
from item.views.item_view import ItemView

app_name = 'item'

urlpatterns = [
    path('', ItemView.as_view({"get": "list", "post": "create"}), name='item-list'),
]