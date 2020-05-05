from django.shortcuts import render
from WebApp import forms
from django.http import HttpResponseRedirect


# Create your views here.
def ThankView(request):
    return render(request, 'MyApp/thanks.html')


def Emp_View(request):
    form = forms.EmpForm()
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/thanks')
    else:
        form = forms.EmpForm()
    return render(request, 'MyApp/welcome.html', {'form': form})

