from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['trajet', 'numero_place', 'passager','date_reservation','client']  # Liste des champs que vous souhaitez inclure dans le formulaire