from django import forms
from django_countries.fields import CountryField

DELIVERY_METHODS = (
	('P', 'PICKUP'),
	('D', 'DELIVERY')
)


class CheckOutForm(forms.Form):
	email = forms.EmailField(max_length=256)
	deliveryFirstName = forms.CharField(max_length=30)
	deliveryLastName = forms.CharField(max_length=30)
	deliveryCompany = forms.CharField(max_length=50, required=False)

	deliveryMethod = forms.ChoiceField(
		widget=forms.RadioSelect, choices=DELIVERY_METHODS
	)

	deliveryStreet = forms.CharField(max_length=256)
	deliveryStreetNum = forms.CharField(max_length=20)
	deliveryCity = forms.CharField(max_length=256)
	deliveryPostal = forms.CharField(max_length=10)
	# deliveryCountry = forms.CountryField(blank_label=('select a country') )
	deliveryPhone = forms.CharField(max_length=20, required=False)

	billingFirstName = forms.CharField(max_length=30)
	billingLastName = forms.CharField(max_length=30)
	billingCompany = forms.CharField(max_length=50, required=False)

	billingStreet = forms.CharField(max_length=256)
	billingStreetNum = forms.CharField(max_length=20)
	billingCity = forms.CharField(max_length=256)
	billingPostal = forms.CharField(max_length=10)
	# billingCountry = forms.CountryField()
	billingPhone = forms.CharField(max_length=20, required=False)