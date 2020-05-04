from django.db import models

from ..shopping_cart_app.models import ShoppingCart
from ..store_app.models import Product


# Create your models here.
class SearchHistory(models.Model):
	"""
	Django model for the orders placed in the store.
	"""

	time = models.DateField()
	# productname = models.ForeignKey(Product.productname, on_delete=CASCADE) þarf ekki lika nafnið?


class Profile(models.Model):
	"""
	Django model for the profile of the user.
	"""

	profileName = models.CharField(
		max_length=200
	)
	profileEmail = models.EmailField()
	profileImage = models.ImageField()
	shoppingCartID = models.ForeignKey(
		"ShoppingCart"
	)
	searches = models.ManyToManyField(
		"SearchHistory",
		through=SearchHistory
	)

	def get_addresses(self, **kwargs):
		"""
		Get all addresses and returns them
		"""
		return Address.objects.all()

	def get_shopping_cart(self, **kwargs):
		return ShoppingCart.objects.all()


class Postal(models.Model):
	"""
	Django model for the postal information of the user.
	"""

	postalCode = models.DecimalField()
	city = models.CharField(
		max_length=60
	)


class Address(models.Model):
	"""
	Django model for the address of the user.
	"""

	profileID = models.ForeignKey(
		"Profile",
		on_delete=models.CASCADE()
	)
	street = models.CharField(
		max_length=200
	)
	house_num = models.CharField(
		max_length=200
	)
	postalID = models.ForeignKey(
		"Postal",
		on_delete=models.CASCADE()
	)

	def get_postal_info(self, **kwargs):
		return Postal.objects.all()


h = Profile()
h.get_addresses()
