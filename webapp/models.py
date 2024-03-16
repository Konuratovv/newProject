from django.db import models

# Create your models here.


class MyModel(models.Model):
    field = models.CharField(max_length=50)