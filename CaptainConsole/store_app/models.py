from django.db import models


class Product(models.Model):
    """
    Django model for the store's products.
    """
    GAME = 'Game'
    CONSOLE = 'Console'
    MISC = 'Misc'
    PRODUCT_TYPE_CHOICES = [
        (GAME, 'Video game'),
        (CONSOLE, 'Console'),
        (MISC, 'Misc.'),
    ]

    name = models.CharField(max_length=256)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPE_CHOICES)
    manufacturer = models.CharField(max_length=256)
    year = models.CharField(max_length=4)
    price = models.DecimalField(decimal_places=2, max_digits=100, null=False, blank=False)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    active = models.BooleanField(default=True)

    def get_images(self):
        return ProductImage.objects.filter(product=self)

    def __str__(self):
        return str(self.name)


class ProductImage(models.Model):
    """
    Django model for the images of a product.
    """
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="media/product_img/", height_field=None, width_field=None, max_length=None
    )
    main = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    """displayOrder = models.SmallIntegerField()"""

    def __str__(self):
        return f"{str(self.product.name)} - image{self.id}"

class Order(models.Model):
    """
    Django model for the orders placed in the store.
    """
    profile = models.ForeignKey("profile_app.Profile", blank=True, null=True, on_delete=models.CASCADE)
    processed = models.BooleanField(default=False)
    orderDiscount = models.DecimalField(max_digits=3, decimal_places=2)
    items = models.ManyToManyField("Product", through="OrderItem")

    email = models.EmailField(max_length=256)
    deliveryFirstName = models.CharField(max_length=30)
    deliveryLastName = models.CharField(max_length=30)
    deliveryCompany = models.CharField(max_length=50, blank=True, null=True)

    deliveryMethod = models.CharField(max_length=50)
    deliveryPrice = models.DecimalField(max_digits=7, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2)

    deliveryStreet = models.CharField(max_length=256)
    deliveryStreetNum = models.CharField(max_length=20)
    deliveryCity = models.CharField(max_length=256)
    deliveryPostal = models.CharField(max_length=10)
    deliveryCountry = models.CharField(max_length=256)
    deliveryPhone = models.CharField(max_length=20, blank=True, null=True)

    billingFirstName = models.CharField(max_length=30)
    billingLastName = models.CharField(max_length=30)
    billingCompany = models.CharField(max_length=50, blank=True, null=True)

    billingStreet = models.CharField(max_length=256)
    billingStreetNum = models.CharField(max_length=20)
    billingCity = models.CharField(max_length=256)
    billingPostal = models.CharField(max_length=10)
    billingCountry = models.CharField(max_length=256)
    billingPhone = models.CharField(max_length=20, blank=True, null=True)


    def get_total_price(self):
        """ Calculate and return total price of order, taking discounts into account. """
        total = 0
        for item in self.items:
            item_price = item.product.productPrice - (
                item.product.productPrice * (item.itemDiscount / 100)
            )
            total += item.quantity * item_price
        total = total - (total * (self.orderDiscount / 100))
        # Add tax
        total += total * self.tax
        # Add the cost of shipping
        total += self.deliveryPrice
        return total

    def __str__(self):
        return f"Order {self.id}, account: {str(self.profile)}"

class OrderItem(models.Model):
    """
    Django model for the items in an order.
    """
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    itemDiscount = models.DecimalField(max_digits=3, decimal_places=2)
    quantity = models.SmallIntegerField()

    def __str__(self):
        return f"{str(self.order)} - {str(self.product)}"