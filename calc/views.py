from django.shortcuts import render, HttpResponse
from . models import *
import math

def calc(request):
    if request.method == "GET":
        return render(request, "calc/index.html")
    else: 
        try: 
            a = float(request.POST["cislo1"])
            b = float(request.POST["cislo2"])
        except ValueError:
            vysledok = "error"
            return render(request, "calc/index.html", {"vysledok":vysledok})

        operator = request.POST["operator"]

        if operator == "+":
            vysledok = a + b
        elif operator == "-":
            vysledok = a - b
        elif operator == "*":
            vysledok = round(a * b, 2)
        elif operator == "/" and b != 0:
            vysledok = round(a / b, 2)
        else:
            vysledok = "error"
            return render(request, "calc/index.html", {"vysledok":vysledok, "cislo1":a, "cislo2":b, "operator":operator})
        try:
            priklad_check = Priklad.objects.get(a = a, b = b, operator = operator)
        except:
            priklad = Priklad(
                a = a,
                b = b,
                operator = operator,
                vysledok = vysledok,
            )
            priklad.save()
        
        return render(request, "calc/index.html", {"vysledok":vysledok, "cislo1":a, "cislo2":b, "operator":operator})