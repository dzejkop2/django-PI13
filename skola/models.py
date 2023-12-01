from django.db import models

class Trieda(models.Model):
    nazov = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nazov}"

class Student(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.trieda}"

class Ucitel(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
    titul = models.CharField(max_length=20)

    def __str__(self):
        if self.trieda:
            return f"{self.titul} {self.meno} {self.priezvisko} {self.trieda}"
        else:
            return f"{self.titul} {self.meno} {self.priezvisko}"