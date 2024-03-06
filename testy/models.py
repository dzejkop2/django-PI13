from django.db import models

class High_score(models.Model):
    score = models.IntegerField()

    def __str__(self):
        return f"{self.score}"