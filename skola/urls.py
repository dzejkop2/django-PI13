from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_student, name='vypis-students'),
]
