from django.contrib import admin
from WebApp.models import Emp

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['EmpId','EmpName','EmpSal','EmpAdd']
admin.site.register(Emp,EmpAdmin)