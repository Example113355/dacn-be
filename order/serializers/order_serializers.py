from rest_framework import serializers
from order.models import Order, OrderItem
from item.serializers.item_serializer import ItemSerializer
from authentication.serializers.user_serializer import UserSerializer
from order.serializers.order_item_serializers import OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'total_price', 'items']


class CreateOrderSerializer(serializers.Serializer):
    test = serializers.IntegerField()
