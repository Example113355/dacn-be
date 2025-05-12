from django.contrib import admin

# Register your models here.
from order.models import Order, OrderItem


class ItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'created_at')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    inlines = [ItemInline]

admin.site.register(Order, OrderAdmin)
