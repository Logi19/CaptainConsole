from django import forms
import django_countries
from django_countries.widgets import CountrySelectWidget

from .models import Order, OrderItem

DELIVERY_METHODS = (
	'PICKUP',
	'DELIVERY'
)


class CheckOutForm(forms.ModelForm):

	class Meta:
		model = Order
		exclude = ['items', 'profile', 'processed', 'orderDiscount', 'tax', 'deliveryPrice']
		widgets = {'country': CountrySelectWidget()}
	# 	email = forms.EmailField(max_length=256)
	# 	deliveryFirstName = forms.CharField(max_length=30)
	# 	deliveryLastName = forms.CharField(max_length=30)
	# 	deliveryCompany = forms.CharField(max_length=50, required=False)
	# 	deliveryMethod = forms.ChoiceField(
	# 		widget=forms.RadioSelect, choices=DELIVERY_METHODS
	# 	)
	# 	deliveryStreet = forms.CharField(max_length=256)
	# 	deliveryStreetNum = forms.CharField(max_length=20)
	# 	deliveryCity = forms.CharField(max_length=256)
	# 	deliveryPostal = forms.CharField(max_length=10)
	# 	deliveryCountry = forms.CountryField().formfield
	# 	deliveryPhone = forms.CharField(max_length=20, required=False)
	#
	# 	billingFirstName = forms.CharField(max_length=30)
	# 	billingLastName = forms.CharField(max_length=30)
	# 	billingCompany = forms.CharField(max_length=50, required=False)
	#
	# 	billingStreet = forms.CharField(max_length=256)
	# 	billingStreetNum = forms.CharField(max_length=20)
	# 	billingCity = forms.CharField(max_length=256)
	# 	billingPostal = forms.CharField(max_length=10)
	# 	billingCountry = CountryField()
	# 	billingPhone = forms.CharField(max_length=20, required=False)


class OrderItem(forms.ModelForm):

	class Meta:
		model = OrderItem
		exclude = ['quantity']