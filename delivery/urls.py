from django.urls import path, include
from delivery.views import DeliveryView


urlpatterns = [
    path("", DeliveryView.as_view({"get": "list", "post": "create"})),
    path("<str:order_code>/", DeliveryView.as_view({"get": "retrieve"})),
]
