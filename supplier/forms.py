from django.forms import ModelForm
from . models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["created_on","updated_on", "supplier_id"]
