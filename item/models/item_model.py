from django_core.models import BaseModel
from django.db import models


class Item(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    is_seed = models.BooleanField(default=False)
    growth_period = models.CharField(max_length=100, null=True, blank=True)
    sun_condition = models.IntegerField(null=True, blank=True)
    water_condition = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
