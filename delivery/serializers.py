from rest_framework import serializers
from delivery.models import Delivery


class DeliveryItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    quantity = serializers.IntegerField()
    price = serializers.IntegerField()


class GetDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = "__all__"


class CreateDeliverySerializer(serializers.Serializer):
    to_name = serializers.CharField()
    to_phone = serializers.CharField()
    to_address = serializers.CharField()
    to_ward_name = serializers.CharField()
    to_district_name = serializers.CharField()
    to_province_name = serializers.CharField()
    items = DeliveryItemSerializer(many=True)
    weight = serializers.IntegerField(default=1)
