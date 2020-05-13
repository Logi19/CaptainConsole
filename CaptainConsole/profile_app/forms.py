from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import HiddenInput, TextInput
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='First name', required=False)
    last_name = forms.CharField(max_length=30, label='Last name', required=False)
    profileImage = forms.ImageField(required=False, label='Profile image')

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profileImage')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, label='Email', help_text='Required.')
    first_name = forms.CharField(max_length=30, label='First name', required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, label='Last name', required=True, help_text='Required.')
    profileImage = forms.ImageField(required=False, label='Profile image', help_text='Optional.')

    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name', 'profileImage', 'password1', 'password2')
