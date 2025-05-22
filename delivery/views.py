import requests
from django.conf import settings

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from delivery.models import Delivery
from delivery.serializers import GetDeliverySerializer, CreateDeliverySerializer


class DeliveryView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return CreateDeliverySerializer(*args, **kwargs)
        return GetDeliverySerializer(*args, **kwargs)
    
    def get_queryset(self):
        return Delivery.objects.filter(user=self.request.user)
    
    def list(self, request):
        deliveries = self.get_queryset()
        serializer = self.get_serializer(deliveries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["payment_type_id"] = 2
        serializer.validated_data["service_type_id"] = 2
        serializer.validated_data["required_note"] = "KHONGCHOXEMHANG"

        response = requests.post(
            "https://dev-online-gateway.ghn.vn/shiip/public-api/v2/shipping-order/create",
            json=serializer.validated_data,
            headers={
                "Token": settings.GHN_TOKEN,
                "ShopId": settings.GHN_SHOP_ID,
            }
        )

        print(response.status_code)

        if response.status_code != 200:
            return Response(
                {"error": "Failed to create delivery order"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data = response.json().get("data")

        if not data:
            return Response(
                {"error": "Invalid response from GHN API"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        Delivery.objects.create(
            user=request.user,
            fee = data.get("total_fee"),
            order_code=data.get("order_code"),
            expected_delivery_time=data.get("expected_delivery_time"),
            phone=serializer.validated_data["to_phone"],
            address = f"{serializer.validated_data['to_address']}, {serializer.validated_data['to_ward_name']}, {serializer.validated_data['to_district_name']}, {serializer.validated_data['to_province_name']}"
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, order_code):
        if not order_code:
            return Response(
                {"error": "order_code is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        response = requests.post(
            "https://dev-online-gateway.ghn.vn/shiip/public-api/v2/shipping-order/detail",
            headers={
                "Token": settings.GHN_TOKEN,
                "ShopId": settings.GHN_SHOP_ID,
            },
            json={
                "order_code": order_code
            }
        )
        
        if response.status_code != 200:
            return Response(
                {"error": "Failed to retrieve delivery order"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data = response.json().get("data")

        return Response(data, status=status.HTTP_200_OK)
