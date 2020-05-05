from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.

def media(request):
    if request.method =='POST' and request.FILES['file']:
        file1 = request.FILES['file']
        fileurl = FileSystemStorage().url(FileSystemStorage().save(file1.name,file1))
+        return render(request,'media.html',{'uploadedfileurl':fileurl})

    return render(request,'media.html')

from webapp.forms import practiceform
from django.http import HttpResponseRedirect

def mediaform(request):
    if request.method =='POST' :
        form1 = practiceform(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect('/Home')
    else:
        form1 = practiceform()
        return render(request,'modelform_upload.html',{'form':form1})


def home(request):
    return render(request,'home.html')