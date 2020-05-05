from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from WebApp.forms import SignUpForm
from django.http import HttpResponseRedirect


# Create your views here.
def Home_Page(request):
    return render(request, 'MyApp/home.html')


@login_required
def Customer(request):
    return render(request, 'MyApp/customer.html')


def Logout_View(request):
    return render(request, 'MyApp/logout.html')


def Registration_View(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, "MyApp/registration.html", {'form': form})
