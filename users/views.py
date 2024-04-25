# Импортируем функции render и redirect из модуля django.shortcuts
from django.shortcuts import render, redirect
# Импортируем форму создания пользователя из модуля django.contrib.auth.forms
from django.contrib.auth.forms import UserCreationForm
# Импортируем функции login и authenticate из модуля django.contrib.auth
from django.contrib.auth import login, authenticate
# Импортируем декоратор login_required из модуля django.contrib.auth.decorators
from django.contrib.auth.decorators import login_required
# Импортируем модель пользователя из модуля django.contrib.auth.models
from django.contrib.auth.models import User
# Импортируем модуль messages из django.contrib для работы с сообщениями
from django.contrib import messages


@login_required  # Декорируем функцию edit_profile декоратором login_required, чтобы ограничить доступ к этой странице только авторизованным пользователям
def edit_profile(request):
    user = request.user  # Получаем текущего пользователя из запроса

    if request.method == 'POST':  # Проверяем, был ли запрос методом POST
        # Если да, то обрабатываем данные формы для обновления профиля пользователя
        # Пример:
        # user.username = request.POST['username']
        # user.email = request.POST['email']
        # user.save()
        # Добавляем сообщение об успешном обновлении профиля
        messages.success(request, 'Profile updated successfully.')
        # Перенаправляем пользователя на страницу профиля
        return redirect('users:profile')

    # Отображаем шаблон edit_profile.html с данными пользователя
    return render(request, 'users/edit_profile.html', {'user': user})


def signup(request):
    if request.method == 'POST':  # Проверяем, был ли запрос методом POST
        # Создаем форму на основе полученных данных
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Проверяем, являются ли данные валидными
            form.save()  # Сохраняем данные пользователя
            # Получаем имя пользователя из валидных данных формы
            username = form.cleaned_data.get('username')
            # Получаем пароль пользователя из валидных данных формы
            raw_password = form.cleaned_data.get('password1')
            # Аутентифицируем пользователя
            user = authenticate(username=username, password=raw_password)
            login(request, user)  # Авторизуем пользователя
            # Перенаправляем пользователя на страницу профиля
            return redirect('users:profile')
    else:
        # Если запрос не методом POST, создаем новую форму для регистрации пользователя
        form = UserCreationForm()
    # Отображаем шаблон signup.html с формой для регистрации пользователя
    return render(request, 'users/signup.html', {'form': form})


@login_required  # Декорируем функцию profile_view декоратором login_required, чтобы ограничить доступ к этой странице только авторизованным пользователям
def profile_view(request):
    user = request.user  # Получаем текущего пользователя из запроса
    # Отображаем шаблон profile.html с данными пользователя
    return render(request, 'users/profile.html', {'user': user})
