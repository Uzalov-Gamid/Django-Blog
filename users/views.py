from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


@login_required
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        # Обновляем данные пользователя, включая фото профиля, если оно было загружено
        user_form = UserForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('users:profile')
    else:
        user_form = UserForm(instance=user)

    return render(request, 'users/edit_profile.html', {'user_form': user_form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('users:profile')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})
