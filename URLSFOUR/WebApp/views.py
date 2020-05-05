from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def Home(request):
    return HttpResponse("<a href='/hi'>Hello</a>")
def MyView(request):
    return HttpResponseRedirect(reverse('bye'))
def ByeView(request):
    return HttpResponse("GoodBye")
