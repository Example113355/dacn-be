from django.db import models
from django_core.models import BaseModel
from authentication.models import User


class Delivery(BaseModel):
    class DeliveryStatusChoices(models.TextChoices):
        PENDING = "pending", "Pending"
        IN_PROGRESS = "in_progress", "In Progress"
        DELIVERED = "delivered", "Delivered"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="deliveries")
    fee = models.IntegerField(default=0)
    order_code = models.CharField(max_length=255, unique=True)
    expected_delivery_time = models.DateTimeField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=DeliveryStatusChoices.choices,
        default=DeliveryStatusChoices.PENDING,
    )
