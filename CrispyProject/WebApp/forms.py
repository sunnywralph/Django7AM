from django import forms
from WebApp.models import Person


# Fields with Validation
class EmpForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
