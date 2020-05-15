from django import forms

from django_countries.fields import CountryField

from .models import Order, OrderItem

DELIVERY_METHODS = (
	('P', 'PICKUP'),
	('D', 'DELIVERY')
)


class CheckOutForm(forms.ModelForm):
	""" The form for receiving the Order model and process that to html for the user to put into data """

	class Meta:
		""" The meta class of the Check Out form """
		model = Order
		exclude = ['items', 'profile', 'processed',
				   'orderDiscount', 'tax',
				   'deliveryPrice', 'deliveryCountry',
				   'billingCountry'
				   ]
	# widgets = {'country': CountrySelectWidget()}

	email = forms.EmailField(widget=forms.EmailInput(attrs={
		'placeholder': 'bobby@johnson.com',
		'class': 'input-field col s6',
		'style': 'height: 20px; ' 
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px;'
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				'color: white;'
	}))
	deliveryFirstName = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'John',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	deliveryLastName = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'Doe',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'
	}))


	deliveryCompany = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'placeholder': 'Captain Console',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	deliveryMethod = forms.ChoiceField(
		widget=forms.RadioSelect, choices=DELIVERY_METHODS, required=False
	)
	deliveryStreet = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'Menntavegur',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	deliveryStreetNum = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': '1',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	deliveryCity = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'Reykjavik',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	deliveryPostal = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': '102',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	deliveryCountry = CountryField().formfield()
	deliveryPhone = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'placeholder': '5812345',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	billingFirstName = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'John',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	billingLastName = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'Doe',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	billingCompany = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'placeholder': 'Captain Console',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))

	billingStreet = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'Menntavegur',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	billingStreetNum = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': '1',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	billingCity = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'Reykjavik',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'
	}))
	billingPostal = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': '102',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	billingCountry = CountryField().formfield()
	billingPhone = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'placeholder': '5812345',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 45%;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))


class OrderItem(forms.ModelForm):
	class Meta:
		model = OrderItem
		exclude = ['quantity']
