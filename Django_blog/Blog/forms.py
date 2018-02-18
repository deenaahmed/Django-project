from django import forms
from .models import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class commentform(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)

class RegistrationForm(UserCreationForm):
	class Meta:
		model=User
		fields=("username","email","password1","password2")