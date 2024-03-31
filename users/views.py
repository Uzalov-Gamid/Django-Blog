from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpRequest
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_passwd)
            login(request, user)
            return redirect('/')

    else:

        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})
