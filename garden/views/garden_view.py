from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from garden.models.garden_model import Garden
from garden.serializers.garden_serializer import GardenSerializer, CreateGardenSerializer

from item.models.item_model import Item

class GardenView(viewsets.ModelViewSet):
    serializer_class = GardenSerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return CreateGardenSerializer(*args, **kwargs)
        return GardenSerializer(*args, **kwargs)

    def get_queryset(self):
        return Garden.objects.filter(user=self.request.user).prefetch_related('item')
    
    def list(self, request):
        return Response(
            GardenSerializer(Garden.objects.filter(user=request.user).prefetch_related('item'), many=True).data,
            status=status.HTTP_200_OK
        )
        
    def create(self, request):
        if not Item.objects.filter(id=request.data["item_id"]).exists():
            return Response({"message": "Item does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not Item.objects.filter(id=request.data["item_id"]).filter(is_seed=True).exists():
            return Response({"message": "Item is not a seed"}, status=status.HTTP_400_BAD_REQUEST)

        request.data['user_id'] = request.user.id

        serializer = CreateGardenSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)