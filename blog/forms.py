from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    tags = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Post
        fields = ['content']
