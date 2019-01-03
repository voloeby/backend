from django import forms
from russianseasons.models import *


class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemPrototype
        fields = ['colors', 'sizes', 'price']
