from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def MyView(request,val1,val2,val3):
    Msg=val1+" "+val2+" "+val3+" "+"Home Page"
    return HttpResponse(Msg)


