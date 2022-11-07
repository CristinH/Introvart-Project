from django import forms
from django.contrib.auth.forms import UserCreationForm
from.models import User

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nume de utilizator'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Introduceți adresa de email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Introduceți parola'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirmați parola'}))
    class Meta:
        model=User
        fields=["username","email","password1","password2"]