from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Intent
from django import forms

class CreateUserForm(UserCreationForm):
  class Meta:
    model=User
    fields=['username','email','password1','password2']

class IntentForm(ModelForm):
  class Meta:
    model=Intent
    fields="__all__"
