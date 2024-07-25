from django.shortcuts import render
from .models import Cities


def cities(request):
    attractions = Cities.objects.all()
    return render(request, 'cities/cities.html', {'attractions': attractions})
