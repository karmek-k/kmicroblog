from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.order_by('-id')
    
    return render(request, 'blog/index.html', {'posts': posts})


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('blog:index')
    
    return render(request, 'blog/add_post.html', {'form': PostForm})
