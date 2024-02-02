from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('categories/', views.categories, name='categories'),
    path('customers/', views.customers, name='customers'),
    path("categories/<category>", views.category, name="category"),
    path("<product>", views.product, name="product")
]