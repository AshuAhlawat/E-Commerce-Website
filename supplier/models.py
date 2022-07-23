from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(default="untitled", max_length=100)
    desciption = models.CharField(max_length=1000,blank=True)
    category = models.CharField(default="unclassified",max_length=30)

    image = models.ImageField(upload_to="images/products/", default="default/product.jpeg")

    price = models.PositiveIntegerField(default=100)
    discount = models.FloatField(default=0.0)

    pack_of = models.PositiveIntegerField(default=1)
    units = models.PositiveIntegerField(default=1)
    in_stock = models.BooleanField(default=True)

    supplier_id = models.IntegerField(default=1)

    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} x {self.units}"