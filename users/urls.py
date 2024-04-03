from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/signup/', views.signup, name='login_signup'),
]
