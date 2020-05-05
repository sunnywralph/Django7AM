from django.contrib import admin
from WebApp.models import Person


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Job_Title', 'Biodata']


admin.site.register(Person, PersonAdmin)
