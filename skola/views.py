from django.shortcuts import render,HttpResponse
from . models import *

def vypis_skola(request):
    triedy = Trieda.objects.all().order_by("nazov")
    studenti = Student.objects.all().order_by("priezvisko")
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"triedy":triedy, "ucitelia":ucitelia, "studenti":studenti})

def vypis_studenti(request):
    studenti = Student.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"studenti":studenti})

def vypis_triedy(request):
    triedy = Trieda.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {"triedy":triedy})

def vypis_ucitelia(request):
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"ucitelia":ucitelia})

def vypis_trieda(request, trieda):
    trieda_obj = Trieda.objects.get(nazov=trieda)
    studenti = Student.objects.filter(trieda_id=trieda_obj.pk).order_by("priezvisko")
    studenti_list = []
    for student in studenti:
        studenti_list.append(student)
    ucitel = Ucitel.objects.get(trieda_id=trieda_obj.pk)
    id_ucitel = f"{ucitel.id}"
    ucitel = f"{ucitel.titul} {ucitel.meno} {ucitel.priezvisko}"
    return render(request, "skola/trieda_list.html", {"trieda":trieda,"ucitel":ucitel,"studenti":studenti_list,"id":id_ucitel})

def vypis_ucitel(request,ucitel):
    ucitel_obj = Ucitel.objects.get(id=ucitel)
    trieda = ucitel_obj.trieda
    meno = f"{ucitel_obj.titul} {ucitel_obj.meno} {ucitel_obj.priezvisko}" 
    id = f"{ucitel_obj.id}"
    return render(request, "skola/ucitel_detail.html", {"ucitel":meno, "trieda":trieda, "id":id})

def vypis_student(request,student):
    student_obj = Student.objects.get(id=student)
    trieda = student_obj.trieda
    ucitel_obj = Ucitel.objects.get(trieda=trieda)
    meno = f"{student_obj.meno} {student_obj.priezvisko}"
    triedny = f"{ucitel_obj.titul} {ucitel_obj.meno} {ucitel_obj.priezvisko}" 
    id = f"{ucitel_obj.id}"
    return render(request, "skola/student_detail.html", {"student":meno, "trieda":trieda, "triedny":triedny,"id":id})
