from django.shortcuts import render

# Create your views here.

from .models import Flight, Passenger

def index(request):
    return render(request, "flights/index.html", {"flights": Flight.objects.all()})

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight, 
        "passengers": flight.passengers.all()
    })
    