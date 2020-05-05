from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home_Page(request):
    return HttpResponse("<h1>Welcome To Home Page</h1>")
def Index_Page(request,year):
    return HttpResponse(f'Welcome To Index Page Of- {year}')