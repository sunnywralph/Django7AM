from django.shortcuts import render
from django.core import validators
from django.core.exceptions import ValidationError

# Create your views here.
def validateEmail(email):
	try:
		validate_email(email)
		return True
	except ValidationError:
		return False