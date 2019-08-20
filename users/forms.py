from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  # django already has registration form templates that we can use
from .models import Profile

class UserRegisterForm(UserCreationForm): # inherits from UserCreationForm
    email = forms.EmailField()

    class Meta:
        # meta model establishes the model we want UserRegisterForm to interact with and what fields we want to display
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
