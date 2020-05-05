from django.shortcuts import render

# Create your views here.
def My_View(request):
    return render(request,'template/welcome.html')
