from django.shortcuts import render,redirect
from supplier.models import Product
from .models import Customer,Cart,Item
from .forms import CustomerForm


# Create your views here.
def home(request):
    uclassified = Product.objects.filter(category="unclassified")
    classified = Product.objects.filter(category="classified")

    context = {
        "cats" : [uclassified, classified]
    }
    # print(dict(request.session))

    if request.session.has_key("user"):
        customer = Customer.objects.get(username=request.session["user"])
        context["customer"] = customer

        
        if request.method == "POST":
            p_id = request.POST["id"]
            amount = request.POST["amount"]

            product = Product.objects.get(id=p_id)
            item = Item(product=product, amount=amount)
            present = 0
            kart = Cart.objects.get(owner=customer)
            cartItems = kart.items.all()
            for i in range(len(cartItems)):
                cart_item = cartItems[i]
                if(item.product.id == cart_item.product.id):
                    present = 1
                    cart_item.amount += int(item.amount)
                    cart_item.save()
                    break

            if(not present):
                item.save()
                kart.items.add(item)
                kart.save()

            
    return render(request, "customer/home.html", context)

def profile(request):
    try:
        name = request.session["user"]
        customer = Customer.objects.get(username=name)
    except:
        return redirect("/customer/login")

    data = {
        "customer" : customer
    }

    return render(request, "customer/profile.html", data)

def cart(request):
    try:
        name = request.session["user"]
        customer = Customer.objects.get(username=name)
        cart = Cart.objects.get(owner=customer)
        cartitems = cart.items.all()
    except:
        customer = ""
        cartitems = []

    context = {
        "customer": customer,
        "cart" : cartitems
    }
    return render(request, "customer/cart.html", context)

def register(request):
    error = ""
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer = customer_form.save()
            cart = Cart(owner=customer)
            cart.save()

            return redirect("/")
        else:
            error = "Usermame already takem"
    else:
        customer_form = CustomerForm()
        
    context = {
        "customer_form" : customer_form,
        "error" : error
    }

    return render(request, "customer/register.html", context)

def login(request):
    error = ""
    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")        
        
        try:
            customer = Customer.objects.get(username=user)
            if password== customer.password:
                print("Yaay right pass")
                request.session["user"] = user
                return redirect("/")
            else:
                error = "Wromg Password"
        except:
            error = "User Doest exist"

    print(error)

    context = {
        "error" : error
    }

    return render(request, "customer/login.html", context)

def delete_item(request):

    Item.objects.get(id=request.GET["id"]).delete()

    return redirect("/customer/cart")
    