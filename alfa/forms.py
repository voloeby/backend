from django.db import models
from django import forms
from alfa.models import *

class ThemeForm(forms.ModelForm):
	class Meta:
		model = Theme
		fields = ['name']
		widgets = {
			'name': forms.widgets.TextInput(attrs={'class': 'form-control rounded-0 ', 'required': ''}),
		}
		labels = {
			'name': 'Theme',
		}

class YesArgumentForm(forms.ModelForm):
	class Meta:
		model = YesArgument
		fields = ['text']
