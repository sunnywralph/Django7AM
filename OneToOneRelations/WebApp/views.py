from django.shortcuts import render
from .models import State


def statelist(request):
    items = State.objects.all()
    return render(request, 'MyApp/StateCapital.html', {'items': items})
