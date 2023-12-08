from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_blog, name='vypis-blog'),
    path('authors/', views.vypis_authors, name='vypis-authors'),
    path('categories/', views.vypis_kategorie, name='vypis-kategorie'),
]
