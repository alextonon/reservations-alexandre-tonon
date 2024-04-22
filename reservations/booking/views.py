from django.shortcuts import render, get_list_or_404

from .models import Trajet

def trajets(request):
    trajets = get_list_or_404(Trajet.objects.all())
    return render(request, 'booking/trajets.html', {'trajets': trajets})
