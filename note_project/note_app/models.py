from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=40)
    desc = models.CharField(max_length=200)
    def __str__(self) -> str:
        return "title: {}\ndescription: {}\n".format(self.title, self.desc)

class Note(models.Model):
    title = models.CharField(default='', max_length=40)
    desc = models.CharField(default='', max_length=200)
    is_done = models.BooleanField(default=False)
    # category = models.ForeignKey(Category, on_delete=CASCADE)

    def __str__(self) -> str:
        return "title: {}\ndescription: {}\n".format(self.title, self.desc)