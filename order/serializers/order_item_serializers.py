from rest_framework import serializers
from order.models import Order, OrderItem
from item.serializers.item_serializer import ItemSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = OrderItem
        fields = ['item_id', 'item', 'quantity', 'price']
