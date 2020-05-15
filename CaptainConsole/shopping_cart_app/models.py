from django.db import models


class ShoppingCart(models.Model):
    """
	Django model for a shopping cart. Can either be connected to an account or temporary.
	"""

    items = models.ManyToManyField("store_app.Product", through="ShoppingCartItem")

    def get_total_price(self):
        """ Calculates total price of order. """
        total = 0
        for item in ShoppingCartItem.objects.filter(shoppingCart=self.id):
            total += item.get_price()

        return round(total, 2)

    def __str__(self):
        return str(self.id)


class ShoppingCartItem(models.Model):
    """
	Django model for items in a shopping cart
	"""

    shoppingCart = models.ForeignKey("ShoppingCart", on_delete=models.CASCADE)
    item = models.ForeignKey("store_app.Product", on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()

    def get_price(self):
        """ Returns price for item instance. """
        return round(self.quantity * self.item.price, 2)

    def __str__(self):
        return f"{str(self.shoppingCart)} - {str(self.item)}, {self.quantity}"
