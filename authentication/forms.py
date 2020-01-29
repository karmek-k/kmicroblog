from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from captcha.fields import CaptchaField


class CaptchaUserCreationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = get_user_model()
        fields = ['username']
