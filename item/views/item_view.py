from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from item.models.item_model import Item
from item.serializers.item_serializer import ItemSerializer


class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def list(self, request):
        return Response(
            ItemSerializer(Item.objects.all(), many=True).data,
            status=status.HTTP_200_OK
        )

    def create(self, request):
        serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
