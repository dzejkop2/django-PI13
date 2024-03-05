from django.shortcuts import render,HttpResponse
import random

from calc.models import *

def test(request):
    priklady = Priklad.objects.all()
    random_priklad = random.choice(priklady)
    if request.method == "GET":
        return render(request, "testy/index.html", {"priklad":random_priklad})

    else:
        try: 
            vysledok = float(request.POST["vysledok"])
        except ValueError:
            vysledok = "error"
            return render(request, "testy/index.html", {"priklad":random_priklad,"vysledok":vysledok})
        
        if float(request.POST["vysledok"]) == float(request.POST["priklad_vysledok"]):
            test = "nice"
        else:
            test = "nn"
        return render(request, "testy/index.html", {"priklad":random_priklad,"test":test})