from django.urls import path  # Импортируем функцию path из модуля django.urls
# Импортируем представления для аутентификации из модуля django.contrib.auth под псевдонимом auth_views
from django.contrib.auth import views as auth_views
from . import views  # Импортируем представления из текущего приложения

app_name = 'users'  # Указываем имя приложения для пространства имен URL

urlpatterns = [  # Определяем список URL-шаблонов
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'),  # URL для страницы входа пользователя
    # URL для страницы регистрации пользователя
    path('signup/', views.signup, name='signup'),
    # URL для страницы просмотра профиля пользователя
    path('profile/', views.profile_view, name='profile'),
    # URL для страницы редактирования профиля пользователя
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
