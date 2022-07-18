from django.db import models

# Create your models here.
class Cart(models.Model):
    items = models.ManyToManyField("supplier.Product")

    def total(self):
        items_list = self.items.all()

        total = 0
        disc = 0

        for item in items_list:
            total += item.price
            disc += item.price*0.01*item.discount
        
        return total-disc

    def __str__(self):
        items_list = self.items.all()
        return f"{len(items_list)} - Items for {self.total()}"
