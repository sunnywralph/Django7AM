from django import forms
from webapp.models import document

class practiceform(forms.ModelForm):
    class Meta:
        model = document
        fields ='__all__'
