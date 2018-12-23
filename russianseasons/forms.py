from django import forms
from russianseasons.models import *


class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemPrototype
        fields = ['colors', 'sizes', 'price']


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'content']
        widgets = {
            'title': forms.widgets.TextInput(attrs={'class': 'my-2 mp-0 rounded-0', 'style': 'width:100%'}),
        }
        labels = {
            'title': 'Заголовок',
            'content': '',
        }
