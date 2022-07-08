from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import forms
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, EmailInput, PasswordInput, CharField, EmailField

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'forms-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'forms-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'forms-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'forms-input'}))
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }