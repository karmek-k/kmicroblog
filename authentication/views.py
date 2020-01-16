from django.shortcuts import render, redirect

from .forms import CaptchaUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = CaptchaUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('authentication:signup')
        return redirect('blog:index')

    return render(request, 'registration/signup.html', {
        'form': CaptchaUserCreationForm()
    })
