from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from django.http import HttpRequest
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            data = timezone.now()
            author = request.user
            title = form.cleaned_data.get("title")
            subtitle = form.cleaned_data.get("subtitle")
            img = form.cleaned_data.get("img")
            description = form.cleaned_data.get("description")
            post = Post(author=author, data=data, title=title,
                        subtitle=subtitle, img=img, description=description)
            post.save()

            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form})


class PostViev(View):
    '''вывод записей'''

    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'main/index.html', {'post_list': posts})


class PostDetail(View):
    '''отдельная страница записи'''

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'main/main_detail.html', {'post': post})
