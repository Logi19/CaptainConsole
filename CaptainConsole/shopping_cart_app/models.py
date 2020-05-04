from django.db import models


class ShoppingCart(models.Model):
    """
	Django model for a shopping cart. Can either be connected to an account or temporary.
	"""

    items = models.ManyToManyField("store_app.Product", through=ShoppingCartItem)

    def __str__(self):
        # TODO: implement detail view functionality
        return self.items


class ShoppingCartItem(models.Model):
    """
	Django model for items in a shopping cart
	"""

    shoppingCart = models.ForeignKey("ShoppingCart", on_delete=models.CASCADE)
    item = models.ForeignKey("store_app.Product", on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
