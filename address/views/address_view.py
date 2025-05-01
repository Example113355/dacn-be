from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from address.exceptions import AddressAlreadyExists, AddressNotOwner
from address.models.address_model import Address
from address.serializers.address_serializer import AddressSerializer, UpdateAddressSerializer
from authentication.serializers.user_serializer import UserSerializer

class AddressView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user).select_related("user")
    
    def get_serializer_class(self):
        if self.action == "update":
            return UpdateAddressSerializer
        return AddressSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        user_serializer = UserSerializer(request.user)
        
        return Response({
            "user": user_serializer.data,
            "addresses": serializer.data
        }, status=status.HTTP_200_OK)
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        address_validated = serializer.validated_data
        
        if Address.objects.filter(
            user=request.user,
            address=address_validated.get("address"),
            phone=address_validated.get("phone")
        ).exists():
            raise AddressAlreadyExists()
        
        address = serializer.save(user=request.user)
        
        return Response({
            "address": AddressSerializer(address).data
        }, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        address_validated = serializer.validated_data
        
        address = Address.objects.get(id=address_validated.get("id"))
        
        if address.user != request.user:
            raise AddressNotOwner()
        
        if Address.objects.filter(
            user=request.user,
            address=address_validated.get("address"),
            phone=address_validated.get("phone")
        ).exists():
            raise AddressAlreadyExists()
        
        address.address = address_validated.get("address")
        address.phone = address_validated.get("phone")
        address.save()
        
        return Response({
            "address": AddressSerializer(address).data
        }, status=status.HTTP_200_OK)