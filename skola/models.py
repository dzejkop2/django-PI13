from django.db import models

class Student(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.trieda}"

class Ucitel(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.CharField(max_length=20)
    titul = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.titul} {self.meno} {self.priezvisko} {self.trieda}"