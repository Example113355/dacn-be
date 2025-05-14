from rest_framework import serializers
from garden.models.garden_model import Garden, CaringType
from item.serializers.item_serializer import ItemSerializer
from authentication.serializers.user_serializer import UserSerializer


class GardenSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    user = UserSerializer()

    class Meta:
        model = Garden
        fields = '__all__'
        

class CreateGardenSerializer(serializers.ModelSerializer):
    item_id = serializers.IntegerField()
    plant_id = serializers.IntegerField()
    user_id = serializers.IntegerField(allow_null=True, required=False)
    class Meta:
        model = Garden
        fields = "status", "item_id", "user_id", "plant_id"


class CaringGardenSerializer(serializers.ModelSerializer):
    garden_item_id = serializers.IntegerField()
    caring_type = serializers.ChoiceField(choices=CaringType.choices)

    class Meta:
        model = Garden
        fields = "garden_item_id", "caring_type"
