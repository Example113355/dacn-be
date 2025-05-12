from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction

from garden.models.garden_model import Garden
from garden.serializers.garden_serializer import GardenSerializer, CreateGardenSerializer, CaringGardenSerializer

from history.history_models import History

from item.models.item_model import Item

class GardenView(viewsets.ModelViewSet):
    serializer_class = GardenSerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return CreateGardenSerializer(*args, **kwargs)
        elif self.action == 'caring':
            return CaringGardenSerializer(*args, **kwargs)
        return GardenSerializer(*args, **kwargs)

    def get_queryset(self):
        return Garden.objects.filter(user=self.request.user).prefetch_related('item')
    
    def list(self, request):
        return Response(
            GardenSerializer(Garden.objects.filter(user=request.user).prefetch_related('item'), many=True).data,
            status=status.HTTP_200_OK
        )
        
    @transaction.atomic
    def create(self, request):
        if not Item.objects.filter(id=request.data["item_id"]).exists():
            return Response({"message": "Item does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        item = Item.objects.get(id=request.data["item_id"])

        if not item.is_seed:
            return Response({"message": "Item is not a seed"}, status=status.HTTP_400_BAD_REQUEST)

        request.data['user_id'] = request.user.id

        serializer = CreateGardenSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()

        History.objects.create(
            user=request.user,
            description=f"Created a garden with item {serializer.data['item_id']}",
            is_caring_history=True,
            garden_item=Garden.objects.get(id=serializer.data['id']),
            caring_type=History.CareType.GROWING,
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def caring(self, request):
        user = request.user
        garden = Garden.objects.filter(user=user, item_id=request.data["garden_item_id"]).first()
        caring_type = request.data["caring_type"]

        if not garden:
            return Response({"message": "Garden does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        if caring_type == History.CareType.WATERING:
            History.objects.create(
                user=user,
                description=f"Watered the garden with item {garden.item.name}",
                is_caring_history=True,
                garden_item=garden,
                caring_type=History.CareType.WATERING,
            )
        
        elif caring_type == History.CareType.FERTILIZING:
            History.objects.create(
                user=user,
                description=f"Fertilized the garden with item {garden.item.name}",
                is_caring_history=True,
                garden_item=garden,
                caring_type=History.CareType.FERTILIZING,
            )

        elif caring_type == History.CareType.HARVESTING:
            History.objects.create(
                user=user,
                description=f"Harvested the garden with item {garden.item.name}",
                is_caring_history=True,
                garden_item=garden,
                caring_type=History.CareType.HARVESTING,
            )

            garden.delete()

        return Response(
            {"message": f"Successfully {caring_type.lower()} the garden with item {garden.item.name}"},
            status=status.HTTP_200_OK
        )
