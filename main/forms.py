from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(label='id_title', max_length=100)
    subtitle = forms.CharField(label='id_subtitle', max_length=300)
    img = forms.ImageField(label='id_img')
    description = forms.CharField(label='id_description', widget=forms.Textarea)