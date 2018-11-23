from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from russianseasons.models import *
from bs4 import BeautifulSoup
from django.urls import reverse

class CheckboxWidget(forms.CheckboxSelectMultiple):
	def render(self, *args, **kwargs):
		output = super(CheckboxWidget, self).render(*args, **kwargs)
		soup = BeautifulSoup(output, 'html.parser')
		ul = soup.ul
		ul.name = 'div'
		for li in ul.findAll('li'):
			li.name = 'div'
			li['class'] = 'form-check'
			print(li)
		for label in ul.findAll('label'):
			label['class'] = 'form-check-label'
		for label in ul.findAll('input'):
			label['class'] = 'form-check-input'
		ul.append(soup.new_tag('a'))
		ul.a['class'] = 'btn btn-primary mt-3'
		ul.a['href'] = reverse(self.url_name)

		ul.a.append(self.button_text)
		return soup.__str__()

class ColorCheckboxWidget(CheckboxWidget):
	button_text = 'Добавить цвет'
	url_name = 'new_color_url'

class SizeCheckboxWidget(CheckboxWidget):
	button_text = 'Добавить размер'
	url_name = 'new_size_url'

class LoginForm(forms.Form):
	username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
	password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

class ItemForm(forms.ModelForm):
	colors = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), widget=ColorCheckboxWidget(), label='Цвета:')
	sizes = forms.ModelMultipleChoiceField(queryset=Size.objects.all(), widget=SizeCheckboxWidget(), label='Размеры:')
	class Meta:
		model = ItemPrototype
		fields = ['name', 'description', 'price', 'colors', 'sizes', 'image']
		widgets = {
			'name': forms.widgets.TextInput(attrs={'class': 'form-control'}),
			'description': forms.widgets.Textarea(attrs={'class': 'form-control',}),
			'price': forms.widgets.NumberInput(attrs={'class': 'form-control',})
			# 'colors': forms.widgets.CheckboxInput(attrs={'class': 'form-control',}),

		}
		labels = {
			'name': 'Название:',
			'description': 'Описание:',
			'colors': 'Цвета:',
			'price': 'Цена:',
		}

class TextInputForm(forms.Form):
	text = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}), label='')

class AnotherInputForm(forms.ModelForm):
	class Meta:
		model = Storage
		fields = ['key', 'value']
		widgets = {
			'key': forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'required': ''}),
			'value': forms.Textarea(attrs={'autofocus': True, 'class': 'form-control', 'rows': '7',}),
		}
		labels = {
			'key': 'Название:',
			'value': 'Значение',
			}
