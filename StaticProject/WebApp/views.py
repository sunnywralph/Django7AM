from django.shortcuts import render
from datetime import datetime
# Create your views here.
def dateinfo(request):
    dt_now=datetime.now()
    name="Python Django"
    th=int(dt_now.strftime('/%H'))
    if th<12:
        wish="Hey Good Morning"
    elif th<16:
        wish="Say Hey Good Noon"
    else:
        wish="Good Night Guys"
    PyDict={'name':name,'dt_now':dt_now,'wish':wish}
    return render(request,'MyApp/Welcome.html',PyDict)
