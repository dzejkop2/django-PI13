from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    text = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name} {self.cost}"
    
class Customer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product} {self.customer} {self.date}"