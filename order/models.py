from django.db import models
from django_core.models import BaseModel
from authentication.models.user import User
from item.models.item_model import Item


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    items = models.ManyToManyField(Item, through='OrderItem')

    def __str__(self):
        return f"{self.user.username} - {self.total_price} - {self.created_at}"

class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.order.user.username} - {self.item.name} - {self.quantity} - {self.price}"
