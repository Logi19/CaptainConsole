from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import HiddenInput, TextInput

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

