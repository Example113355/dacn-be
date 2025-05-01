from rest_framework import serializers
from garden.models.garden_model import Garden
from item.serializers.item_serializer import ItemSerializer


class GardenSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Garden
        fields = '__all__'