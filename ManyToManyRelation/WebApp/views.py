from django.shortcuts import render
from WebApp.models import Driver


def driverslist(request):
    items = Driver.objects.all()
    return render(request, 'MyApp/CarDriver.html', {'items': items})
