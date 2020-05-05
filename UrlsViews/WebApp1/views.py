from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def MyHomePage(request):
    return HttpResponse("<h2 style='color:black';font-size='90px';font-family='tahoma';text-decoration='overline'>Say Hey Django</h2>")