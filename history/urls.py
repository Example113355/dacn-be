from django.urls import path
from history.views import HistoryView


urlpatterns = [
    path('history/', HistoryView.as_view({'get': 'list'}), name='history-list'),
]
