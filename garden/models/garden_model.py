from django_core.models import BaseModel
from django.db import models
from item.models.item_model import Item


class Garden(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.item.name