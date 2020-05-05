from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home_Page(request):
    return HttpResponse("<h1 font='tahoma'>Hello Django</h2>")