from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    content = models.TextField()
    votes = models.IntegerField(default=0)
    op = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OP')
    created_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='tags')

    def __str__(self):
        return str(self.content)[:50]
