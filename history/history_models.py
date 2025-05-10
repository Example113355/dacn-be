from django.db import models
from django_core.models import BaseModel
from garden.models.garden_model import Garden
from authentication.models.user import User

# Create your models here.

class History(BaseModel):
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_caring_history = models.BooleanField(default=False)
    garden_item = models.ForeignKey(Garden, on_delete=models.CASCADE, null=True, blank=True)
