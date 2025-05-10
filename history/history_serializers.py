from rest_framework import serializers
from history.history_models import History
from authentication.serializers.user_serializer import UserSerializer
from garden.serializers.garden_serializer import GardenSerializer


class HistorySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    garden_item = GardenSerializer(allow_null=True, required=False)
    
    class Meta:
        model = History
        fields = '__all__'
