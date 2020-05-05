from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Company


# Create your views here.
def org_retrive(request, id=None):
    instance = get_object_or_404(Company, id=id)
    context = {'instance': instance}
    return render(request, "MyApp/retrive.html", context)
