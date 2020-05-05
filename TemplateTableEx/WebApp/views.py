from django.shortcuts import render

# Create your views here.
def My_Home(request):
    return render(request,'template/Welcome.html')
def Thanks(request):
    return render(request,'template/Thanks.html')