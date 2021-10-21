from django.db import models
from django.db.models.base import Model

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)