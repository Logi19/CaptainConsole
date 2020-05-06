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

    productName = models.CharField(max_length=256)
    productType = models.CharField(max_length=50, choices=PRODUCT_TYPE_CHOICES)
    productManufacturer = models.CharField(max_length=256)
    productYear = models.CharField(max_length=4)
    productPrice = models.IntegerField()
    productDescription = models.TextField(blank=True)

    def get_images(self):
        return ProductImage.objects.filter(product=self)

    def __str__(self):
        return str(self.productName)


class ProductImage(models.Model):
    """
    Django model for the images of a product.
    """
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="media/product_img/", height_field=None, width_field=None, max_length=None
    )
    displayOrder = models.SmallIntegerField()

    def __str__(self):
        return f"{str(self.product)} - image{self.id}"

class Order(models.Model):
    """
    Django model for the orders placed in the store.
    """
    profile = models.ForeignKey("profile_app.Profile", blank=True, null=True, on_delete=models.CASCADE)
    processed = models.BooleanField(default=False)
    orderDiscount = models.DecimalField(max_digits=3, decimal_places=2)
    items = models.ManyToManyField("Product", through="OrderItem")

    def get_total_price(self):
        """ Calculate and return total price of order, taking discounts into account. """
        total = 0
        for item in self.items:
            item_price = item.product.productPrice - (
                item.product.productPrice * (item.itemDiscount / 100)
            )
            total += item.quantity * item_price
        total = total - (total * (self.orderDiscount / 100))
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