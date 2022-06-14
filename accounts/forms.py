from distutils.command.upload import upload
import profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','first_name','last_name','email', )

class UpdateUserForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ['username','first_name','last_name','email', 'profile_pic']