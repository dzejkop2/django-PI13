from django.shortcuts import render
import random

from calc.models import *
from . models import *

def test(request):
    priklady = Priklad.objects.all()
    random_priklad = random.choice(priklady)
    high_score = High_score.objects.all()[0]
    current_score = 0
    if request.method == "GET":
        return render(request, "testy/index.html", {"priklad":random_priklad, "high_score":high_score, "current_score":current_score})

    else:
        try: 
            vysledok = float(request.POST["vysledok"])
        except ValueError:
            vysledok = "error"
            return render(request, "testy/index.html", {"priklad":random_priklad,"vysledok":vysledok,"high_score":high_score, "current_score":current_score})
        
        current_score = int(request.POST["current_score"])

        if float(request.POST["vysledok"]) == float(request.POST["priklad_vysledok"]):
            test = "Správne"
            current_score += 1
        else:
            test = "Nesprávne"
            current_score = 0
        
        if current_score > high_score.score:
            high_score.score = current_score
            high_score.save()

        return render(request, "testy/index.html", {"priklad":random_priklad,"test":test,"high_score":high_score, "current_score":current_score})