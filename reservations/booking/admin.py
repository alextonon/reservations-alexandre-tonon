from django.contrib import admin

from .models import Gare
from .models import Trajet

admin.site.register(Gare)
admin.site.register(Trajet)
