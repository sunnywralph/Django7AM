from .models import Student
from django import forms


class StdForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Stdno', 'Stdname', 'Profpic', 'StdAdd']
