from django.shortcuts import render, get_list_or_404, get_object_or_404,redirect

from .models import Trajet
from .models import Reservation

from .forms import ReservationForm

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

@login_required
def edit_reservation(request, numero_reservation=None):
    if numero_reservation == None:
        reservation = None
    else:
        reservation = get_object_or_404(Reservation, pk=numero_reservation)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save()
            reservation.client = request.user
            return redirect('booking:reservation_details', numero_reservation=reservation.numero_reservation)
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'booking/edit_reservation.html', {'form': form})