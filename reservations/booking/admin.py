from django.contrib import admin


from .models import Gare
from .models import Trajet
from .models import Passager
from .models import Reservation

admin.site.register(Gare)
admin.site.register(Trajet)
admin.site.register(Passager)
admin.site.register(Reservation)
