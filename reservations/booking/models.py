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

class Passager(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()

    def __str__(self):
        return f'{self.nom} {self.prenom}'
    
    
class Reservation(models.Model):
    numero_reservation = models.CharField(max_length=100, primary_key=True)
    numero_place = models.IntegerField()
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(default=datetime.now)
    passager = models.ForeignKey(Passager, on_delete=models.CASCADE)
    client = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return f'{self.nom} {self.prenom} ({self.trajet})'