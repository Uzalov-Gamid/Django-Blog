from django.urls import path
from . import views

# app_name = 'main'

urlpatterns =[
    path('', views.PostViev.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]

