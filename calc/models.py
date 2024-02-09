from django.db import models

class Priklad(models.Model):
    a = models.FloatField()
    b = models.FloatField()
    operator = models.CharField(max_length=1)
    vysledok = models.FloatField()

    def __str__(self):
        return f"{self.a} {self.operator} {self.b} = {self.vysledok}"