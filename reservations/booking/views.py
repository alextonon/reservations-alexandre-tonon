from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Trajet
from .models import Reservation

from django.contrib.auth.decorators import login_required
from django import forms

def trajets(request):
    trajets = get_list_or_404(Trajet.objects.all())
    return render(request, 'booking/trajets.html', {'trajets': trajets})

@login_required
def reservations(request):
    reservations = get_list_or_404(Reservation, client=request.user)
    return render(request, 'booking/reservations.html', {'reservations': reservations})

@login_required
def reservation_details(request, numero_reservation):
    reservation = get_object_or_404(Reservation, pk=numero_reservation)
    return render(request, 'booking/reservation.html', {'reservation': reservation})