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

	}))


class OrderItem(forms.ModelForm):
	class Meta:
		model = OrderItem
		exclude = ['quantity']
