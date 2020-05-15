from django import forms

from django_countries.fields import CountryField

from .models import Order, OrderItem

DELIVERY_METHODS = (("P", "PICKUP"), ("D", "DELIVERY"))


class CheckOutForm(forms.ModelForm):
    """ The form for receiving the Order model and process that to html for the user to put into data """

    class Meta:
        """ The meta class of the Check Out form """

        model = Order
        exclude = [
            "items",
			"profile",
            "processed",
            "orderDiscount",
            "tax",
            "deliveryPrice",
            "deliveryCountry",
            "billingCountry",
        ]

    # widgets = {'country': CountrySelectWidget()}

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px;"
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        )
    )
    deliveryFirstName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        )
    )
    deliveryLastName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        )
    )

    deliveryCompany = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Company (optional)",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        ),
    )
    deliveryMethod = forms.ChoiceField(
        widget=forms.RadioSelect, choices=DELIVERY_METHODS, required=False,
    )
    deliveryStreet = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Street name",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        )
    )
    deliveryStreetNum = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Street number",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        )
    )
    deliveryCity = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "City",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        )
    )
    deliveryPostal = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Postal code",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        )
    )
    deliveryCountry = CountryField(blank_label="Delivery country").formfield()
    deliveryPhone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        ),
    )
    billingFirstName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        )
    )
    billingLastName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        )
    )
    billingCompany = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Company (optional)",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        ),
    )

    billingStreet = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Street name",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        )
    )
    billingStreetNum = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Street number",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        )
    )
    billingCity = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "City",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        )
    )
    billingPostal = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Postal code",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        )
    )

    billingCountry = CountryField(blank_label="Billing country").formfield()

    billingPhone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone",
                "class": "input-field col s6",
                "style": "height: 20px; "
                "width: 45%;"
                "padding: 7px; "
                "margin-top: 10px; "
                "margin-bottom: 10px; "
                "font-size: 20px;"
                "color: white;",
            }
        ),
    )


class OrderItem(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = ["quantity"]
