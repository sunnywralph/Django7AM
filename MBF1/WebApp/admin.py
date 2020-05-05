from django.contrib import admin
from WebApp.models import Emp


# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Salary']
admin.site.register(Emp,EmpAdmin)
