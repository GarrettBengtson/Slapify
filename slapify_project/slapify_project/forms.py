from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=[('user', 'User'), ('artist', 'Artist')])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')
