from .views import HomePageView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, PostNewView, PostEditView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/',
         LoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='signup.html'),
         name='signup'),
    path('new/',
         PostNewView.as_view(template_name='post_new.html'),
         name='post_new'),
    path('post/<int:pk>/',
        PostEditView.as_view(template_name='post_detail.html'),
        name='post_detail'),

]