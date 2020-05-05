from django import forms
from WebApp.models import Emp


# Fields with validations
class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'
