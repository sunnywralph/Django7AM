from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Test_Cookie(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>We are Testing Cookies..!!</h1>")


def Check_Cookie(request):
    if request.session.test_cookie_worked():
        print("Say Hey Cookies are Working Fine..!!")
        request.session.delete_test_cookie()
        return HttpResponse("<h1>Cookies are Deleted...!</h1>")