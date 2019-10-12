from django import forms
from russianseasons.models.Message import Message
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV3

class MessageForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Message
        fields = ['name', 'email', 'text']
