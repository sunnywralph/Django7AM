from django.shortcuts import render
import datetime
# Create your views here.
def dateInfo(request):
    date = datetime.datetime.now()
    name = 'NareshIT-Ameerpet'
    txt = int(date.strftime('%H'))
    if txt<12:
        wish = "Morning Buddy"
    elif txt<16:
        wish = "Good Afternoon-Dude"
    else:
        wish = "Good Night Guys"
    Py_Dict = {'date': date,'name': name,'wish': wish}
    return render(request,'MyApp/welcome.html', context=Py_Dict)
