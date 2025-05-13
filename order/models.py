from django.db import models
from django_core.models import BaseModel
from authentication.models.user import User
from item.models.item_model import Item


class Order(BaseModel):
    class OrderStatus(models.TextChoices):
        PENDING = 'pending', 'Pending'
        COMPLETED = 'completed', 'Completed'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    items = models.ManyToManyField(Item, through='OrderItem')
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
    )
    order_code = models.IntegerField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.total_price} - {self.created_at}"

class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.item.name} - {self.quantity} - {self.price}"
