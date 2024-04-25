from django import forms
from django.forms import PasswordInput, EmailInput

class RegisterForm(forms.Form):
    user_name = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=PasswordInput)
    email = forms.CharField(label='Email', widget=EmailInput)
