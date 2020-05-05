from django.shortcuts import render
from WebApp.models import Emp

# Create your views here.
def Emp_View(request):
    EmpList=Emp.objects.all()
    My_Dict={'elist':EmpList}
    return render(request,'MyApp/welcome.html',My_Dict)
