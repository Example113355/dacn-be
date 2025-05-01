from django.urls import path

from address.views.address_view import AddressView

urlpatterns = [
    path(
        "",
        AddressView.as_view({"get": "list", "post": "create", "patch": "update"}),
        name="address"
    )
]
