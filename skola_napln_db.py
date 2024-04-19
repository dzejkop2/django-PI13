import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import *
import datetime
import random
import csv

Trieda.objects.all().delete()
Student.objects.all().delete()
Ucitel.objects.all().delete()

triedy = []

arr = []

with open('ULICE.csv', mode ='r') as file:
    csvFile = csv.reader(file,delimiter=";")
    for lines in csvFile:
        arr.append(lines)

for rocnik in range(1,5):
    for pismeno in ["A","B","C","D"]:
        triedy.append(f"{rocnik}.{pismeno}")
        Trieda.objects.create(nazov=f"{rocnik}.{pismeno}")

fmena = open("mena.txt", "r", encoding="utf-8")
mena = fmena.read().splitlines()

fpriezviska = open("priezviska.txt", "r", encoding="utf-8")
priezviska = fpriezviska.read().splitlines()

def get_vek(trieda_temp):
    if(trieda_temp[0] == "1"):
        return 16
    elif(trieda_temp[0] == "2"):
        return 17
    elif(trieda_temp[0] == "3"):
        return 18
    else:
        return 19

def get_date(vek):
    today = datetime.date.today()
    start_date = datetime.date(today.year - vek, 1, 1)
    end_date   = datetime.date(today.year - vek, 12, 31)
    num_days   = (end_date - start_date).days
    rand_days   = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)
    return random_date

for i in range(20):
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    vek = random.randrange(26,65)
    narodenie = get_date(vek)
    bydlisko=random.choice(arr)
    ulica = bydlisko[0] + " " + str(random.randrange(1,150))
    psc = bydlisko[1]
    obec = bydlisko[2]
    titul = random.choice(["Mgr.", "Ing.", "PhDr.", "PaeDr.",""])
    if i < len(triedy):
        trieda = Trieda.objects.get(nazov=triedy[i])
        Ucitel.objects.create(meno=meno,priezvisko=priezvisko,titul=titul,narodenie=narodenie,psc=psc,ulica=ulica,obec=obec,trieda=trieda)
    else: 
        Ucitel.objects.create(meno=meno,priezvisko=priezvisko,titul=titul,narodenie=narodenie,psc=psc,ulica=ulica,obec=obec)

for i in range(100):
    trieda_temp = random.choice(triedy)
    bydlisko=random.choice(arr)
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    trieda = Trieda.objects.get(nazov=trieda_temp)
    vek = get_vek(trieda_temp)
    narodenie = get_date(vek)
    ulica = bydlisko[0] + " " + str(random.randrange(1,150))
    psc = bydlisko[1]
    obec = bydlisko[2]
    Student.objects.create(meno=meno,priezvisko=priezvisko,trieda=trieda,psc=psc,ulica=ulica,obec=obec,narodenie=narodenie)
