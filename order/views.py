from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Prefetch


from order.models import Order, OrderItem
from order.serializers.order_serializers import OrderSerializer, CreateOrderSerializer
from order.serializers.order_item_serializers import OrderItemSerializer


class OrderView(viewsets.ModelViewSet):
    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return CreateOrderSerializer(*args, **kwargs)
        return OrderSerializer(*args, **kwargs)
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related(
            Prefetch('items', queryset=OrderItem.objects.select_related('item'))
        )
    
    def list(self, request):
        orders = self.get_queryset()
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        print(request.data)
        return Response({
            "success": True,
        }, status=status.HTTP_200_OK)
