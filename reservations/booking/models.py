from django.db import models
from datetime import datetime

class Gare(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Trajet(models.Model):
    gare_depart = models.ForeignKey(Gare, on_delete=models.CASCADE, related_name='gare_depart')
    gare_arrivee = models.ForeignKey(Gare, on_delete=models.CASCADE, related_name='gare_arrivee')
    heure_depart = models.DateTimeField()
    heure_arrivee = models.DateTimeField()
    

    def __str__(self):
        return f'{self.gare_depart} -> {self.gare_arrivee}'