from django.shortcuts import render
from . models import *

def products(request):
    products = Product.objects.all().order_by("category")
    categories = Category.objects.all().order_by("name")

    return render(request, "shop/index.html", {"products":products, "categories":categories})

def orders(request):
    orders = Order.objects.all().order_by("date")

    return render(request, "shop/index.html", {"orders":orders})

def categories(request):
    categories = Category.objects.all().order_by("name")

    return render(request, "shop/index.html", {"categories":categories})

def customers(request):
    customers = Customer.objects.all().order_by("name")

    return render(request, "shop/index.html", {"customers":customers})

def category(request, category):
    want_category = Category.objects.get(name=category)
    products = Product.objects.filter(category_id=want_category.pk)
    products_list = []

    for i in products:
        products_list.append(f"{i.name}")

    return render(request, "shop/index.html", {"category_products":products_list})

def product(request, product):
    want_product = Product.objects.get(name=product)
    
    return render(request, "shop/produkt.html", {"produkt":want_product})
