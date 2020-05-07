from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import ProfileManager



class Profile(AbstractBaseUser, PermissionsMixin):
    """
    Model for the site's profiles.
    Overrides Django's default 'User' model, changing the username field to use email instead
    and adds other attributes.
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    profileImage = models.ImageField(upload_to='static/media/profile_img/', null=True, blank=True)
    shoppingCart = models.OneToOneField("shopping_cart_app.ShoppingCart", on_delete=models.CASCADE)
    searches = models.ManyToManyField("store_app.Product", through="SearchHistory")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """ Returns the first_name plus the last_name, with a space in between. """
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """ Returns the short name for the user. """
        return str(self.first_name)

    def get_addresses(self):
        """ Returns all addresses associated with the profile. """
        return Address.objects.filter(profile=self)

    def get_shopping_cart(self):
        """ Returns the profile's shopping cart. """
        return ShoppingCart.objects.get(id=self.shoppingCart)

    def __str__(self):
        return self.get_full_name()


class Postal(models.Model):
    """
    Django model for address postal information.
    """

    postalCode = models.CharField(max_length=12)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.postalCode} {self.city}, {self.country}"


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

    def __str__(self):
        return f"{self.street} {self.house_num}"

class SearchHistory(models.Model):
    """
    Django model for profile search history.
    """

    searchProfile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    searchProduct = models.ForeignKey("store_app.Product", on_delete=models.CASCADE)
    # Automatically use current date/time when adding to table
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.searchProfile)} - {str(self.searchProduct)} at {self.time}"