from django import forms
from .models import *

class commentform(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)

class replyform(forms.ModelForm):
	class Meta:
		model = Reply
		fields = ('body',)


