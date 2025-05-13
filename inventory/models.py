from django.db import models
from django_core.models import BaseModel
from authentication.models.user import User
from item.models.item_model import Item


class Inventory(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.email} - {self.item.name} - {self.quantity}"
