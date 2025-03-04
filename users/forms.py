from django import forms
from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import Profile


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control'

            }),
            "email": TextInput(attrs={
                'class': 'form-control'

            }),
            "password1": TextInput(attrs={
                'class': 'form-control',
            }),
            "password2": TextInput(attrs={
                'class': 'form-control'
            })}


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']
