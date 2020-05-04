from django.db import models


class Product(models.Model):
    """
    Django model for the store's products.
    """
    productName = models.CharField(max_length=256)
    productType = models.CharField(max_length=256)
    productYear = models.CharField(max_length=4)
    productPrice = models.IntegerField()
    productDescription = models.TextField(blank=True)

    def get_images(self):
        return ProductImages.objects.filter(product=self)

    def __str__(self):
        return self.productName


class ProductImages(models.Model):
    """
    Django model for the images of a product.
    """
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="product_img", height_field=None, width_field=None, max_length=None
    )


class Order(models.Model):
    """
    Django model for the orders placed in the store.
    """
    profile = models.ForeignKey("profile_app.Profile", on_delete=models.CASCADE)
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


class OrderItem(models.Model):
    """
    Django model for the items in an order.
    """
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    itemDiscount = models.DecimalField(max_digits=3, decimal_places=2)
    quantity = models.SmallIntegerField()
