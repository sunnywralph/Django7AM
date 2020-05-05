from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from .forms import SentForm

def Home(request):
    return render(request,'Home.html')

def sending_mail(request):

    if request.method == 'POST':
        form = SentForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            mail = form.cleaned_data['email']
            sub = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail('got mail from'+str(mail),
                "name: "+str(name)+"\n"
                "email:"+str(mail)+"\n"
                "subject: "+str(sub)+"\n"
                "message :"+ str(message),
                settings.EMAIL_HOST_USER,
                ['sunnywralph@gmail.com'],
                fail_silently=False )
            return HttpResponseRedirect('/Home')
    else:
        form = SentForm()
    return render(request, 'mail.html', {'form': form})
