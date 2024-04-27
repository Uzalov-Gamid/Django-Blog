from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Добавляем поле для фотографии профиля
    avatar = models.ImageField(
        upload_to='avatars/', default='avatars/default.png', blank=True, null=True)

    class Meta:
        managed = True


# Исправляем конфликт имен для полей groups и user_permissions
CustomUser._meta.get_field(
    'groups').remote_field.related_name = 'customuser_set'
CustomUser._meta.get_field(
    'user_permissions').remote_field.related_name = 'customuser_set'
