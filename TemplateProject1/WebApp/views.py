from django.shortcuts import render

# Create your views here.
def MyTemp(request):
    return render(request,'MyApp/Welcome.html')