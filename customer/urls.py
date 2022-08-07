from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('register', views.register),
    path('login', views.login),    
    path('profile', views.profile),
    path('cart', views.cart),
    path('delete_item', views.delete_item)
]