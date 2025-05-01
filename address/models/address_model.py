from django.db import models
from address.exceptions import AddressNotFound
from authentication.models.user import User
from django_core.models import BaseModel

# Create your models here.
class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self):
        return f"{self.user.full_name} - {self.address}"
    
    @staticmethod
    def get_address(user):
        try:
            return Address.objects.get(user=user)
        except Address.DoesNotExist:
            raise AddressNotFound()