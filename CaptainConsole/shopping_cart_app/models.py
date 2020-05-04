from django.db import models


# Create your models here
class ShoppingCart(models.Model):
	items = models.ManyToManyField(through=ShoppingCartItem)

	def __str__(self):
		return self.items


class ShoppingCartItem(models.Model):
	quantity = models.SmallIntegerField()
	shoppingcart = models.ForeignKey("ShoppingCart", on_delete=models.CASCADE)

	def __str__(self):
		return self.quantity


