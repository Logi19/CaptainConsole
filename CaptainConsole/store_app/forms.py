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

	email = forms.EmailField(max_length=256, widget=forms.EmailInput(attrs={
		'placeholder': 'bobby@johnson.com',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px;'
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				'color: white;'
	}))
	deliveryFirstName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
		'placeholder': 'John',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	deliveryLastName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
		'placeholder': 'Doe',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'
	}))


	deliveryCompany = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={
		'placeholder': 'Captain Console',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	deliveryMethod = forms.ChoiceField(
		widget=forms.RadioSelect, choices=DELIVERY_METHODS
	)
	deliveryStreet = forms.CharField(max_length=256, widget=forms.TextInput(attrs={
		'placeholder': 'Menntavegur',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	deliveryStreetNum = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
		'placeholder': '1',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	deliveryCity = forms.CharField(max_length=256, widget=forms.TextInput(attrs={
		'placeholder': 'Reykjavik',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	deliveryPostal = forms.CharField(max_length=10, widget=forms.TextInput(attrs={
		'placeholder': '102',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	billingCountry = CountryField().formfield()
	deliveryPhone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={
		'placeholder': '5812345',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	billingFirstName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
		'placeholder': 'John',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	billingLastName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
		'placeholder': 'Doe',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	billingCompany = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={
		'placeholder': 'Captain Console',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))

	billingStreet = forms.CharField(max_length=256, widget=forms.TextInput(attrs={
		'placeholder': 'Menntavegur',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	billingStreetNum = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
		'placeholder': '1',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	billingCity = forms.CharField(max_length=256, widget=forms.TextInput(attrs={
		'placeholder': 'Reykjavik',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'
	}))
	billingPostal = forms.CharField(max_length=10, widget=forms.TextInput(attrs={
		'placeholder': '102',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
				 'padding: 7px; '
				 'margin-top: 10px; '
				 'margin-bottom: 10px; '
				 'font-size: 20px;'
				 'color: white;'

	}))
	billingCountry = CountryField().formfield()
	billingPhone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={
		'placeholder': '5812345',
		'class': 'input-field col s6',
		'style': 'height: 20px; '
				 'width: 250px;'
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
