from django import forms
from .models import Comment

class commentform(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)

