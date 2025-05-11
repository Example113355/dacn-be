import json
from rest_framework import status, viewsets
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from payos import PayOS, ItemData, PaymentData
from django.conf import settings
from payment.payment_serializers import PaymentSerializer

from django_core.utils import generate_unique_code

PAYOS_CLIENT_ID = settings.PAYOS_CLIENT_ID
PAYOS_API_KEY = settings.PAYOS_API_KEY
PAYOS_CHECKSUM_KEY = settings.PAYOS_CHECKSUM_KEY
FRONT_END_URL = settings.FRONT_END_URL

class PayosService(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def __init__(self):
        self.payOS = PayOS(
            client_id=PAYOS_CLIENT_ID,
            api_key=PAYOS_API_KEY,
            checksum_key=PAYOS_CHECKSUM_KEY,
        )

    def get_serializer(self):
        return PaymentSerializer()

    def create_payment_link(self, request):
        payload = request.data
        serializer = PaymentSerializer(data=payload)

        if not serializer.is_valid():
            return Response({
                "error": serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
        
        items = []
        for item in payload["items"]:
            items.append(ItemData(name=item["item_name"], quantity=item["item_quantity"], price=item["item_price"]))

        payment_data = PaymentData(
            orderCode=generate_unique_code(),
            amount=payload["amount"],
            description=payload["description"],
            items=items,
            cancelUrl=f"{FRONT_END_URL}/cancel",
            returnUrl=f"{FRONT_END_URL}/return",
        )

        payment_link_data = self.payOS.createPaymentLink(paymentData=payment_data)

        return Response(
            {
                "payment_link": payment_link_data.checkoutUrl,
                "account_name": payment_link_data.accountName,
                "amount": payment_link_data.amount,
                "description": payment_link_data.description,
                "order_code": payment_link_data.orderCode,
                "currency": payment_link_data.currency,
                "paymentLinkId": payment_link_data.paymentLinkId,
            },
            status=status.HTTP_200_OK,
        )

        
