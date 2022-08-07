from django.db import models

# Create your models here.
class Cart(models.Model):
    items = models.ManyToManyField("Item")
    owner = models.OneToOneField("Customer", on_delete=models.CASCADE)
    
    def total(self):
        items_list = self.items.all()

        total = 0
        disc = 0

        for item in items_list:
            product = item.product
            total += product.price * item.amount
            disc += product.price*0.01*product.discount* item.amount
        
        return total-disc

    def __str__(self):
        items_list = self.items.all()
        return f"{len(items_list)} - Items for {self.total()}"
    
    def __len__(self):
        return len(self.items.all())

class Item(models.Model):
    product = models.ForeignKey("supplier.Product", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.amount}"

class Customer(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=30)
