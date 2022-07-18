from django.shortcuts import render
from supplier.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()

    context = {
        "products" : products
    }
    return render(request, "customer/home.html", context)