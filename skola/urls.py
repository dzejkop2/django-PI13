from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_skola, name='vypis-skola'),
    path('triedy/', views.vypis_triedy, name='vypis-triedy'),
    path('ucitelia/', views.vypis_ucitelia, name='vypis-ucitelia'),
    path('studenti/', views.vypis_studenti, name='vypis-studenti'),
]
