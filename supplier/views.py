from django.shortcuts import render, redirect
from .forms import ProductForm

# Create your views here.
def home(request):
    return render(request, "supplier/home.html")

def add_product(request):
    if request.method == "GET":
        product_form = ProductForm()

        context = {
            "product_form" : product_form
        }
    elif request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/supplier/home")

    return render(request, "supplier/add_product.html", context)