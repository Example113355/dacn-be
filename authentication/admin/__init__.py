from django.contrib import admin

from authentication.models import *

from .custom_user_admin import UserAdmin

admin.site.register(User, UserAdmin)
