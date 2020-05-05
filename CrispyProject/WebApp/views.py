from django.shortcuts import render
from django.http import HttpResponseRedirect
from WebApp import forms


# Create your views here.
def Emp_View(request):
    form = forms.EmpForm()
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("FORM Data Inserted Successfully")
            return HttpResponseRedirect('/Thanks')
    return render(request, 'MyApp/Welcome.html', {'form': form})


def Thanks(request):
    return render(request, 'MyApp/Thanks.html')
