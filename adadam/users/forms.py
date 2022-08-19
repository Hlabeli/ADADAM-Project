'''
from dataclasses import fields
from attr import attr
from django import forms
from django.forms import TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

Registration fom


class RegistrationForm:
    class Meta:
        model = User
        labels = {'username': '', 'name':'', 'surname': '', 'email_address':'', 'password':'', 'confirm_password':''}
        fields = ['username', 'name', 'surname', 'email_address', 'password', 'confirm_password']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'required': True}),
            'surname': TextInput(attrs={'class': 'form-control', 'required': True}),
            'email_address': EmailInput(attrs={'class': 'form-control', 'required': True}),
            'password': PasswordInput(attrs={'class': 'form-control', 'required': True}),
            'confirm_password': PasswordInput(attrs={'class': 'form-control', 'required': True})
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'forma-control'
        self.fields['confirm_password'].widget.attrs['class'] = 'forma-control'


- Login Form


def LoginForm(AuthenticationForm): 
    class Meta: 
        model = User
        labels = {'username': '', 'password': ''}
        fields = ['password', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
'''