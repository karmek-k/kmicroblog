from django import forms
from captcha.fields import CaptchaField

from .models import Post


class PostForm(forms.ModelForm):
    tags = forms.CharField(max_length=100, required=False)
    captcha = CaptchaField()

    class Meta:
        model = Post
        fields = ['content']
