from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=50, blank=True)
    text = models.TextField(max_length=500)
    def __str__(self):
        return self.text[:50]

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )

class Media(models.Model):
    title = models.CharField(max_length=100, null=True)
    cover = models.ImageField(upload_to='images/')
    book = models.FileField(upload_to='media')
