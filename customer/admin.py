from django.contrib import admin
from . models import Cart,Item,Customer
# Register your models here.

admin.site.register(Cart)
admin.site.register(Item)
admin.site.register(Customer)