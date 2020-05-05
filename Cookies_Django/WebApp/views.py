from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def setcookie(request):
    response = HttpResponse("<h1>Say Hey Cookie Set ..!!</h1>")
    response.set_cookie('user', 'sunny')
    return response


def getcookie(request):
    user = request.COOKIES['user']
    return HttpResponse(user +'Hey Get Cookie Success')


def delcookie(request):
    response = HttpResponse('<h1>Say Hey Cookie Deleted..!!</h1>')
    response.delete_cookie('user')
    return response
