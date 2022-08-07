from django.shortcuts import render, redirect
from .forms import ProductForm
from supplier.models import Product

# Create your views here.
def home(request):
    return render(request, "supplier/home.html")

def product(request, id):
    # print(id)
    product = Product.objects.get(id=id)

    data ={
        'product' : product
    }
    return render(request, "supplier/product.html", data)

def add_product(request):
    if request.method == "GET":
        product_form = ProductForm()

        context = {
            "product_form" : product_form
        }

    elif request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        return redirect("/supplier/home")

    return render(request, "supplier/add_product.html", context)