from django.shortcuts import render
from . models import *

def products(request):
    products = Product.objects.all().order_by("category")

    return render(request, "shop/index.html", {"products":products})

def orders(request):
    orders = Order.objects.all().order_by("date")

    return render(request, "shop/index.html", {"orders":orders})

def categories(request):
    categories = Category.objects.all().order_by("name")

    return render(request, "shop/index.html", {"categories":categories})

def customers(request):
    customers = Customer.objects.all().order_by("name")

    return render(request, "shop/index.html", {"customers":customers})