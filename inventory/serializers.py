from rest_framework import serializers
from inventory.models import Inventory
from item.serializers.item_serializer import ItemSerializer
from authentication.serializers.user_serializer import UserSerializer


class InventorySerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = ['id', 'user', 'item', 'quantity']
