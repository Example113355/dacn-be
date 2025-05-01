from django.contrib import admin

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("address", "phone")}),
    )
    
    list_display = ("address", "phone")
    
    search_fields = ("address", "phone")
    
    list_filter = ("address", "phone")
    
    ordering = ("address", "phone")