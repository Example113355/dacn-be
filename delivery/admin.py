from django.contrib import admin
from delivery.models import Delivery


class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "fee",
        "order_code",
        "expected_delivery_time",
        "phone",
        "address",
        "status",
    )
    search_fields = ("user__username", "order_code", "status")
    list_filter = ("status",)
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    list_per_page = 20

admin.site.register(Delivery, DeliveryAdmin)
