from django.shortcuts import render
from WebApp import forms
from django.http import HttpResponseRedirect
# Create your views here.
def EmpView(request):
    form = forms.EmpForm()
    if request.method =='POST':
        form = forms.EmpForm(request.POST)
