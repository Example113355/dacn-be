from rest_framework import serializers

from address.models.address_model import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("id", "address", "phone")
        

class UpdateAddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    
    class Meta:
        model = Address
        fields = ("id", "address", "phone")