from rest_framework import serializers


class PaymentItemSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    item_name = serializers.CharField(max_length=255)
    item_quantity = serializers.IntegerField(min_value=1)
    item_price = serializers.IntegerField(min_value=1000)


class PaymentSerializer(serializers.Serializer):
    items = PaymentItemSerializer(many=True)
    amount = serializers.IntegerField(min_value=1000)
    description = serializers.CharField(max_length=255)
