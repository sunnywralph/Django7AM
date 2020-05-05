from django.shortcuts import render
from .models import Team


def teamlist(request):
    items = Team.objects.all()
    return render(request, 'MyApp/teamplayer.html', {'items': items})
