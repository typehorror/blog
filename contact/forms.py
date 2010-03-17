from django import forms

from models import Contact

from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ('email_address',
                  'subject',
                  'body',)
