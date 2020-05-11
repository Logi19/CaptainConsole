from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import HiddenInput, TextInput
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, label='Email', help_text='Required.')
    first_name = forms.CharField(max_length=30, label='First name', required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, label='Last name', required=True, help_text='Required.')
    profileImage = forms.ImageField(required=False, label='Profile image', help_text='Optional.')

    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name', 'profileImage', 'password1', 'password2')
