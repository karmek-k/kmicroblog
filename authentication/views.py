from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('authentication:signup')
        return redirect('blog:index')

    return render(request, 'registration/signup.html', {'form': UserCreationForm()})