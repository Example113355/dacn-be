from rest_framework import serializers
from history.history_models import History
from authentication.serializers.user_serializer import UserSerializer


class HistorySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = History
        fields = '__all__'