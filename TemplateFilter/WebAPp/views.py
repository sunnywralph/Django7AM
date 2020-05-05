from django.shortcuts import render
from WebAPp.models import FilterModel

# Create your views here.
def DataView(request):
    datalist = FilterModel.objects.all()
    return render(request,'MyApp/Welcome.html',{'datalist':datalist})