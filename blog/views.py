from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic

from .models import Post, Tag
from .forms import PostForm


class TaggedPostsAbstractListView(generic.ListView):
    template_name = 'blog/list_posts.html'

    def get_context_data(self, **kwargs):
        posts_tags = {}
        for post in self.get_queryset():
            posts_tags.setdefault(post, tuple(post.tags.all()))

        context = super().get_context_data(**kwargs)
        context['posts_tags'] = posts_tags.items()
        return context


class IndexListView(TaggedPostsAbstractListView):
    def get_queryset(self):
        return Post.objects.all()


class TagListView(TaggedPostsAbstractListView):
    def get_queryset(self):
        return Post.objects.filter(tags__name__iexact=self.kwargs['tag_name'])


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.op = request.user
            instance.save()

            # tokenize the tags string and make them lowercase
            tags_list = map(
                lambda s: s.lower().strip(),
                form.cleaned_data['tags'].split()
            )

            # add tags to the new post
            for tag in tags_list:
                tag_queryset = Tag.objects.filter(name=tag)
                if not tag_queryset.exists():
                    t = Tag.objects.create(name=tag)
                else:
                    t = tag_queryset[0]
                instance.tags.add(t)

            form.save_m2m()
        return redirect('blog:index')

    return render(request, 'blog/add_post.html', {'form': PostForm})
