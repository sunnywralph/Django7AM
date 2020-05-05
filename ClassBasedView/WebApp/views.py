from django.views.generic import View
from django.http import HttpResponse


# create your views here.
class CBV(View):
    def get(self, request):
        return HttpResponse("<h1 style='color:red'>Welcome To Class Based Views</h1>")


def post(self, request):
    return HttpResponse("ThankU")
