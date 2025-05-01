from django.db import models
from django_core.models import BaseModel
from authentication.models import User


class Note(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    def __str__(self):
        return self.title
