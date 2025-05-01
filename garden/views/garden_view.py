from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from garden.models.garden_model import Garden
from garden.serializers.garden_serializer import GardenSerializer


class GardenView(viewsets.ModelViewSet):
    serializer_class = GardenSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Garden.objects.all()
    
    def list(self, request):
        return Response(
            GardenSerializer(Garden.objects.all(), many=True).data,
            status=status.HTTP_200_OK
        )
        
    def create(self, request):
        serializer = GardenSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)