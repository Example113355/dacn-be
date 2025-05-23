import json
from rest_framework import status, viewsets
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from payos import PayOS, ItemData, PaymentData
from django.conf import settings
from payment.payment_serializers import PaymentSerializer
from order.models import Order, OrderItem
from item.models.item_model import Item
from inventory.models import Inventory

from django_core.utils import generate_unique_code

PAYOS_CLIENT_ID = settings.PAYOS_CLIENT_ID
PAYOS_API_KEY = settings.PAYOS_API_KEY
PAYOS_CHECKSUM_KEY = settings.PAYOS_CHECKSUM_KEY
FRONT_END_URL = settings.FRONT_END_URL

class PayosService(viewsets.ViewSet):
    def __init__(self):
        self.payOS = PayOS(
            client_id=PAYOS_CLIENT_ID,
            api_key=PAYOS_API_KEY,
            checksum_key=PAYOS_CHECKSUM_KEY,
        )

    def get_permissions(self):
        if self.action == 'payment_webhook':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def payment_webhook(self, request):
        # Verify the webhook data using PayOS SDK
        webhook_data = self.payOS.verifyPaymentWebhookData(request.data)
        if not webhook_data:
            return Response({"error": "Invalid webhook data"}, status=status.HTTP_400_BAD_REQUEST)
        
        order_code = webhook_data.orderCode

        try:
            order = Order.objects.get(order_code=order_code)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        if not order:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        
        order.status = Order.OrderStatus.COMPLETED
        order.save()

        order_items = OrderItem.objects.filter(order=order)
        for order_item in order_items:
            inventory, created = Inventory.objects.get_or_create(
                user=order.user,
                item=order_item.item,
                defaults={"quantity": order_item.quantity},
            )
            if not created:
                inventory.quantity += order_item.quantity
            inventory.save()

        return Response(
            {"success": True},
            status=status.HTTP_200_OK,
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
        item_map = {}
        order_code = generate_unique_code()

        order = Order.objects.create(
            user=request.user,
            total_price=payload["amount"],
            order_code=order_code,
        )

        for item in payload["items"]:
            items.append(ItemData(name=item["item_name"], quantity=item["item_quantity"], price=item["item_price"]))
            item_map[item["item_id"]] = item["item_quantity"]
        
        items_selected = Item.objects.select_for_update().filter(id__in=item_map.keys())
        for item in items_selected:
            OrderItem.objects.create(
                order=order,
                item=item,
                quantity=item_map[item.id],
                price=item.price,
            )

        payment_data = PaymentData(
            orderCode=order_code,
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

        
