from django.shortcuts import render


# Create your views here.
def Hits_View(request):
    hit = request.COOKIES.get('hit', 0)
    newhit = int(hit) + 1
    response = render(request, 'MyApp/hits.html', {'hit': newhit})
    response.set_cookie('hit', newhit)
    return response
