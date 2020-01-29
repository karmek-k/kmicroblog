# from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class MyUserManager(UserManager):
    pass


class User(AbstractUser):
    objects = MyUserManager()
