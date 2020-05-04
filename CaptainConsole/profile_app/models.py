from django.db import models


class SearchHistory(models.Model):
    """
    Django model for profile search history.
    """

    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    product = models.ForeignKey("store_app.Product", on_delete=models.CASCADE)
    # Automatically use current date/time when adding to table
    time = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    """
    Django model for user profiles.
    """

    profileName = models.CharField(max_length=256)
    profileEmail = models.EmailField()
    profileImage = models.ImageField(
        upload_to="profile_img", height_field=None, width_field=None, max_length=None
    )
    shoppingCart = models.ForeignKey(
        "shopping_cart_app.ShoppingCart", on_delete=models.CASCADE
    )
    searches = models.ManyToManyField("SearchHistory", through=SearchHistory)

    def get_addresses(self):
        """ Returns all addresses associated with the profile. """
        return Address.objects.filter(profile=self)

    def get_shopping_cart(self):
        """ Returns the profile's shopping cart. """
        return ShoppingCart.objects.get(id=self.shoppingCart)


class Postal(models.Model):
    """
    Django model for address postal information.
    """

    postalCode = models.CharField(max_length=10)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=256)


class Address(models.Model):
    """
    Django model for profile addresses.
    """

    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    street = models.CharField(max_length=256)
    house_num = models.CharField(max_length=20)
    postal = models.ForeignKey("Postal", on_delete=models.CASCADE)

    def get_postal_info(self):
        return Postal.objects.get(id=self.postal)
