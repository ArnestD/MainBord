from django.views.generic import ListView, CreateView
from .models import Post, Media
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import BaseRegisterForm
from .forms import PostForm
from django.shortcuts import redirect
from render import render
from django.urls import reverse

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'login.html'
    context_object_name = 'user'

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/signup/sing.html'

class PostNewView(CreateView):
    model = Post
    form_class = PostForm
    def PostNewView(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_detail.html', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'post_edit.html', {'form': form})

    def get_success_url(self):
        return reverse('home')

class PostEditView(CreateView):
    model = Post
    form_class = PostForm
    def PostEditView(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_detail.html', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'post_edit.html', {'form': form})

    def get_success_url(self):
        return reverse('home')

def media(request):
    data = Media.objects.all()
    return render(request, 'home.html', {'data': data})

def media_save(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        return render(request, 'home.html', {
            'file_url': file_url
        })
    return render(request, 'home.html')
