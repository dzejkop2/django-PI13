import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import *
import random

Trieda.objects.all().delete()
Student.objects.all().delete()
Ucitel.objects.all().delete()

triedy = []

for rocnik in range(1,5):
    for pismeno in ["A","B","C","D"]:
        triedy.append(f"{rocnik}.{pismeno}")
        Trieda.objects.create(nazov=f"{rocnik}.{pismeno}")

fmena = open("mena.txt", "r", encoding="utf-8")
mena = fmena.read().splitlines()

fpriezviska = open("priezviska.txt", "r", encoding="utf-8")
priezviska = fpriezviska.read().splitlines()


for i in range(20):
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    titul = random.choice(["Mgr.", "Ing.", "PhDr.", "PaeDr.",""])
    if i < len(triedy):
        trieda = Trieda.objects.get(nazov=triedy[i])
        Ucitel.objects.create(meno=meno,priezvisko=priezvisko,titul=titul,trieda=trieda)
    else: 
        Ucitel.objects.create(meno=meno,priezvisko=priezvisko,titul=titul)

for i in range(100):
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    trieda = Trieda.objects.get(nazov=random.choice(triedy))
    Student.objects.create(meno=meno,priezvisko=priezvisko,trieda=trieda)
