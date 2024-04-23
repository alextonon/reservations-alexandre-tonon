from django.contrib import admin
from django.urls import path

from . import views

app_name = 'booking'

urlpatterns = [
    path("trajets", views.trajets, name="trajets"),
    path("reservations", views.reservations, name="reservations"),
    path("reservations/<int:numero_reservation>", views.reservation_details, name="reservation_details"),
    path("reservations/nouvelle_reservation", views.edit_reservation, name="nouvelle_reservation"),
    path("reservations/edit_reservation/<int:numero_reservation>", views.edit_reservation, name="edit_reservation")
]
