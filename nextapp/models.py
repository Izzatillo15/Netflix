from django.db import models


jinsi=(
    ("e","erkak"),
    ("a","ayol")
)







class Actor(models.Model):
    ism = models.CharField(max_length=50)
    sana = models.DateField()
    jins = models.CharField(max_length=2,choices=jinsi)

class Movie(models.Model):
    nom = models.CharField(max_length=50)
    yil = models.DateField()
    imbd = models.DecimalField(max_digits=3,decimal_places=1)
    janr = models.CharField(max_length=50)
    actor = models.ManyToManyField(Actor)