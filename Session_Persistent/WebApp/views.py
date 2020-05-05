from django.shortcuts import render


# Create your views here.
def Page_Hit_View(request):
    hit = request.session.get('hit', 0)
    newhit = hit+1
    request.session['hit'] = newhit
    print("Session expired age:", request.session.get_expiry_age())
    print("Session expired date:", request.session.get_expiry_date())
    return render(request, 'MyApp/hits.html', {'hit': newhit})
