from django.db import models

class Product(models.Model):
    """
    Class for the store's products.
    """
    productName = models.CharField(max_length=256)
    productType = models.CharField(max_length=256)
    productYear = models.CharField(max_length=4)
    productPrice = models.IntegerField()
    productDescription = models.TextField(blank=True)

    def get_images(self):
        return ProductImages.objects.filter(productID=self.pk)

    def __str__(self):
        return self.productName

class ProductImages(models.Model):
    productID = models.ForeignKey("Product", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_img', height_field=None, width_field=None, max_length=None)

class Order(models.Model):
    profileID = models.ForeignKey("profile_app.Profile", on_delete=models.CASCADE)
    orderDiscount = models.DecimalField(max_digits=3, decimal_places=2)
    items = models.ManyToManyField("Product", through="OrderItem")

    def get_total(self):
        pass

class OrderItem(models.Model):
    orderID = models.ForeignKey("Order", on_delete=models.CASCADE)
    productID = models.ForeignKey("Product", on_delete=models.CASCADE)
    itemDiscount = models.DecimalField(max_digits=3, decimal_places=2)
    quantity = models.SmallIntegerField()