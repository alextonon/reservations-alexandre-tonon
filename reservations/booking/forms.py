from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['trajet', 'date_reservation']  # Liste des champs que vous souhaitez inclure dans le formulaire