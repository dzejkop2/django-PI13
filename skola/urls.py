from django.contrib import admin
from django.urls import path, include
from .  import views

urlpatterns = [
    path('', views.vypis_skola, name='skola'),
    path('triedy/', views.vypis_triedy, name='triedy'),
    path('studenti/', views.vypis_student, name='studenti'),
    path('ucitelia/', views.vypis_ucitelov, name='ucitelia'),
    path("triedy/<trieda>/", views.vypis_trieda, name='trieda'),
    path("studenti/<student>/", views.student_detail, name='student'),
    path("ucitelia/<ucitel>/", views.ucitel_detail, name='ucitel'),
    path('kruzky/', views.vypis_kruzky, name='kruzky'),
    path("kruzky/<kruzok>/", views.kruzky_detail, name="kruzok"),
    path('uzivatelpridat/', views.pridat_uzivatel, name='pridat_uzivatel'),
    path('uzivatelpridat2/', views.pridat_uzivatel2, name='pridat_uzivatel2'),

]