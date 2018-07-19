from django.forms import ModelForm
from django import forms
from main.models import *


class Loginform(forms.Form):
	email=forms.EmailField(max_length=100)
	password=forms.SlugField(max_length=30)
	type=forms.CharField(max_length=10)
	isactive=forms.BooleanField()

class LoginForm(ModelForm):
	class Meta:
		model=Login
		fields='__all__'
