from django import forms
class EmpForm(forms.Form):
    Name= forms.charField()
    Salary = forms.integerField()