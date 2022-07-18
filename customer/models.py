from django.db import models

# Create your models here.
class Cart(models.Model):
    items = models.ManyToManyField("supplier.Product")