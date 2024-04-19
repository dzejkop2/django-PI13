from django.db import models

class Trieda(models.Model):
    nazov = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.nazov}'
    
    class Meta:
        verbose_name = "Trieda"
        verbose_name_plural = "Triedy"
        ordering = ['nazov']

class Ucitel(models.Model):
    titul = models.CharField(max_length=20) 
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
    psc = models.CharField(max_length=20, blank=True)
    ulica = models.CharField(max_length=20, blank=True)
    obec = models.CharField(max_length=20, blank=True)
    narodenie = models.DateField(null=True, blank=True)

    def __str__(self):
        if self.trieda:
            return f'{self.titul} {self.meno} {self.priezvisko} {self.trieda}'
        else:
            return f'{self.titul} {self.meno} {self.priezvisko}'
        
    class Meta:
        verbose_name = "Ucitel"
        verbose_name_plural = "Ucitelia"
        ordering = ['priezvisko']

class Kruzok(models.Model):
    nazov = models.CharField(max_length=100)
    skratka = models.CharField(max_length=5)
    ucitel = models.ForeignKey(Ucitel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.skratka} {self.nazov} {self.ucitel}'
    
    class Meta:
        verbose_name = "Kruzok"
        verbose_name_plural = "Kruzky"
        ordering = ['nazov']
    
class Student(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
    kruzok = models.ManyToManyField(Kruzok, blank=True)
    psc = models.CharField(max_length=20, blank=True)
    ulica = models.CharField(max_length=20, blank=True)
    obec = models.CharField(max_length=20, blank=True)
    narodenie = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.meno} {self.priezvisko} {self.trieda}'
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Studenti"
        ordering = ['priezvisko']