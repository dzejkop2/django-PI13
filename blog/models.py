from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"
    
class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    nick = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nick} {self.name} {self.surname}"
    
class Post(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now)   
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.text} {self.author} {self.create_date} {self.publish_date} {self.category}"
    