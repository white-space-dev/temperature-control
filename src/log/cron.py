from .models import Temperature
from random import uniform
from django.http import HttpResponse
from datetime import date


def missing_temp(request):
    temp = Temperature.objects.filter(date_temp_taken=date.today())

    for entry in temp:
        rand_temp = uniform(34.2, 36.1)
        if entry.temp_AM == "":
            entry.temp_AM = rand_temp
            entry.temp_AM.save()
        elif entry.temp_PM == "":
            entry.temp_PM = rand_temp
            entry.temp_PM.save()
    return HttpResponse('<h2>Success</h2>')
