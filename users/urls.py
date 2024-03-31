from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

# app_name = 'main'

urlpatterns =[
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
]