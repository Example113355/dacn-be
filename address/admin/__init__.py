from django.contrib import admin

from address.admin.address_admin import AddressAdmin
from address.models.address_model import Address

admin.site.register(Address, AddressAdmin)