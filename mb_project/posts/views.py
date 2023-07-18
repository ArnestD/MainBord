from django.views.generic import ListView, CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import BaseRegisterForm


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

