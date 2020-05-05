from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import HiddenInput, TextInput

from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ("",)
