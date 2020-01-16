from django.contrib.auth.forms import UserCreationForm

from captcha.fields import CaptchaField


class CaptchaUserCreationForm(UserCreationForm):
    captcha = CaptchaField()
