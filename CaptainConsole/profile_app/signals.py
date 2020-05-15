from django.db.models.signals import pre_save
from django.dispatch import receiver

from shopping_cart_app.models import ShoppingCart
from .models import Profile


@receiver(pre_save, sender=Profile)
def create_shopping_cart(sender, instance, **kwargs):
    """
    Function creates a new shopping cart for a user,
    before the user is saved to the database,
    if they don't already have one.
    """

    # If user doesn't already have shopping cart, create one
    if instance.shoppingCart_id is None:
        cart = ShoppingCart.objects.create()
        instance.shoppingCart = cart
        instance.shoppingCart_id = cart.id
