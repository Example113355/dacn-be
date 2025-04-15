from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("full_name",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_admin")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "full_name", "password1", "password2"),
            },
        ),
    )

    list_display = (
        "email",
        "full_name",
        "is_active",
        "is_staff",
        "is_admin",
    )

    search_fields = (
        "email",
        "full_name",
    )

    ordering = ("email",)
