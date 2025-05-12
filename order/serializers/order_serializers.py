from rest_framework import serializers
from order.models import Order, OrderItem
from item.serializers.item_serializer import ItemSerializer
from authentication.serializers.user_serializer import UserSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    pass
