from .views import HomePageView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, post_new, post_edit

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/',
         LoginView.as_view(template_name = 'login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name = 'signup.html'),
         name='signup'),
    path('post_new/',
         post_new.as_view(template_name = 'post_new.html'),
         name='post_new'),
    path('post/<int:pk>/edit/',
         post_edit.as_view(template_name = 'post_new.html'),
         name='post_edit'),
]