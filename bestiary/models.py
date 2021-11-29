from django.db import models

# Create your models here.


class Monster(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.URLField(blank=True)
    init = models.CharField(max_length=3)
    MV = models.CharField(max_length=25)
    AC = models.IntegerField()
    HD = models.CharField(max_length=6)
    Act = models.CharField(max_length=10)
    alignments = [("L", "Loyal"), ("C", "Chaotic"), ("N", "Neutral")]
    AL = models.CharField(max_length=1, choices=alignments, default="N")
    Atk = models.CharField(max_length=100, blank=True)
    SP = models.TextField(blank=True)
    Spells = models.TextField(blank=True)
    SV = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.AL})."
