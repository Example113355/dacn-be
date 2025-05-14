from django_core.models import BaseModel
from django.db import models


class Item(BaseModel):
    class CategoryChoices(models.TextChoices):
        SEED = 'SEED', 'Seed'
        FERTILIZER = 'FERTILIZER', 'Fertilizer'
        PESTICIDE = 'PESTICIDE', 'Pesticide'
        PLANT = 'PLANT', 'Plant'

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    growth_period = models.CharField(max_length=100, null=True, blank=True)
    sun_condition = models.IntegerField(null=True, blank=True)
    water_condition = models.IntegerField(null=True, blank=True)
    category = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
        default=CategoryChoices.SEED
    )
    plant_item = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='plant_items'
    )
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
