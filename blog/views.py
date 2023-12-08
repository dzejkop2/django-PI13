from django.shortcuts import render
from . models import *

def vypis_blog(request):
    posts = Post.objects.all().order_by("create_date")

    return render(request, "blog/index.html", {"posts":posts})

def vypis_authors(request):
    authors = Author.objects.all().order_by("nick")

    return render(request, "blog/index.html", {"authors":authors})

def vypis_kategorie(request):
    categories = Category.objects.all().order_by("name")

    return render(request, "blog/index.html", {"categories":categories})