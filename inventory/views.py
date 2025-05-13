from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from inventory.models import Inventory
from inventory.serializers import InventorySerializer


class InventoryView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = InventorySerializer

    def get_queryset(self):
        return Inventory.objects.filter(user=self.request.user)
    
    def list(self, request):
        inventories = self.get_queryset()
        serializer = self.serializer_class(inventories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
