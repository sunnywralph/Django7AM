from django import forms
from django.core import validators
#customized
class EmpForm(forms.Form):
    Name = forms.CharField()
    Salary = forms.IntegerField()
    Opinion = forms.CharField()
(widget=forms.Textarea,validators=[validators.MaxlengthValidator(40),validators.MinLengthValidator(10)])