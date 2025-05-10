from django.contrib import admin

# Register your models here.

from history.history_models import History


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('description', 'user', 'is_caring_history', 'garden_item')
    search_fields = ('description', 'user__username', 'garden_item__name')
    list_filter = ('is_caring_history',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'


admin.site.register(History, HistoryAdmin)
