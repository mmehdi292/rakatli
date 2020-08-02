from django.forms import ModelForm
from .models import Mail
from django import forms
from captcha.fields import ReCaptchaField


class SendMailToAdmin(ModelForm):
    class Meta:
        model = Mail
        fields = '__all__'


class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()