from django import forms
from django.contrib.auth.forms import UsernameField
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


class SignInForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=("Password"), strip=False,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ColorCheckboxWidget(CheckboxWidget):
    button_text = 'Добавить цвет'
    url_name = 'new_color_url'


class SizeCheckboxWidget(CheckboxWidget):
    button_text = 'Добавить размер'
    url_name = 'new_size_url'


class LoginForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))


class EditItemForm(forms.ModelForm):
    colors = forms.ModelMultipleChoiceField(
        queryset=Color.objects.all(), widget=ColorCheckboxWidget(), label='Цвета:')
    sizes = forms.ModelMultipleChoiceField(
        queryset=Size.objects.all(), widget=SizeCheckboxWidget(), label='Размеры:')

    class Meta:
        model = ItemPrototype
        fields = ['name', 'category', 'description', 'colors', 'sizes', 'in_stock', 'is_new']
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            # 'sub_name': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'description': forms.widgets.Textarea(attrs={'class': 'form-control', }),
            # 'price': forms.widgets.NumberInput(attrs={'class': 'form-control',}),
            'category': forms.widgets.Select(attrs={'class': 'form-control', }),
            # 'colors': forms.widgets.CheckboxInput(attrs={'class': 'form-control',}),
            'in_stock': forms.widgets.CheckboxInput(attrs={'class': ''}),
            'is_new': forms.widgets.CheckboxInput(attrs={'class': ''}),

        }
        labels = {
            'name': 'Название:',
            'category': 'Категория:',
            'in_stock': 'В наличии:',
            'is_new': 'Новая:',
            # 'sub_name': 'Название кратко',
            'description': 'Описание:',
            'colors': 'Цвета:',
            'price': 'Цена:',
        }


class NewItemForm(forms.ModelForm):
    class Meta:
        model = ItemPrototype
        fields = ['name', 'category', 'description']
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'description': forms.widgets.Textarea(attrs={'class': 'form-control', }),
            'category': forms.widgets.Select(attrs={'class': 'form-control', }),

        }
        labels = {
            'name': 'Название:',
            'category': 'Категория:',
            'description': 'Описание:',
        }


class TextInputForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}), label='')


class AnotherInputForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['key', 'value']
        widgets = {
            'key': forms.TextInput(attrs={'class': 'form-control', 'required': ''}),
            'value': forms.Textarea(attrs={'autofocus': True, 'class': 'form-control', 'rows': '7', }),
        }
        labels = {
            'key': 'Название:',
            'value': 'Значение',
        }


class MainPagePostForm(forms.ModelForm):
    class Meta:
        model = MainPagePost
        fields = ['content']
        labels = {
            'content': '',
        }


class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = ['link', 'image']
        widgets = {
            'link': forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'required': ''}),
        }
        labels = {
            'link': 'Ccылка:',
            'image': 'Изображение:',
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file']


class FinanceForm(forms.ModelForm):
    class Meta:
        model = FinanceItem
        fields = ['money', 'text', 'is_income']
        widgets = {
            'money': forms.NumberInput(attrs={'class': 'form-control', 'required': '', 'min': '0'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '7', }),
            'is_income': forms.CheckboxInput(attrs={'style': 'display:none'}),
        }
        labels = {
            'money': 'Сколько:',
            'text': 'Комментарий:',
            'is_income': '',
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'price', 'sale_price', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': ''}),
            'price': forms.NumberInput(attrs={'class': 'form-control', }),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '7', }),

        }
        labels = {
            'name': 'Название:',
            'price': 'Цена:',
            'sale_price': 'Скидочная цена:',
            'description': 'Описание:',
        }
