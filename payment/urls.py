from django.urls import path

from payment.views import PayosService

urlpatterns = [
    path('', PayosService.as_view({'post': 'create_payment_link'}), name='payment-link'),
    path('webhook/', PayosService.as_view({'post': 'payment_webhook'}), name='payment-webhook')
]
