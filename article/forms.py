from django import forms

from models import Comment

from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ('name',
                  'email_address',
                  'website',
                  'body',)
