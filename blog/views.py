from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Tag
from .forms import PostForm


def index(request):
    posts_tags = {}
    for post in Post.objects.order_by('-id'):
        # posts_tags:s
        # {post1: (tag1, tag2, ...), post2: (), ...}
        posts_tags.setdefault(post, tuple(post.tags.all()))

    return render(request, 'blog/index.html', {'posts_tags': posts_tags.items()})


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.op = request.user
            form.save()
        return redirect('blog:index')
    
    return render(request, 'blog/add_post.html', {'form': PostForm})


def tag(request, tag_name):
    pass
