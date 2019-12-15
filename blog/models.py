from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    content = models.TextField()
    votes = models.IntegerField(default=0)
    op = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)[:50]

