from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(default="untitled", max_length=100)
    desciption = models.CharField(max_length=1000)
    category = models.CharField(default="unclassified",max_length=30)

    image = models.ImageField(upload_to="product_images/")

    price = models.PositiveIntegerField(default=100)
    discount = models.FloatField(default=0.0)

    pack_of = models.PositiveIntegerField(default=1)
    units = models.PositiveIntegerField(default=1)
    in_stock = models.BooleanField(default=True)

    supplier_id = models.IntegerField(default=1)
