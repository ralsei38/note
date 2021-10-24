from django.db import models
from django.db.models.base import Model

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=40)
    desc = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "title: {}\ndescription: {}\n".format(self.title, self.desc)