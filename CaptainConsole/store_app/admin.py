from django.contrib import admin
from .models import Product
from .models import ProductImage


class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['name', 'manufacturer', 'description']
    list_display = ['name', 'type', 'manufacturer', 'year', 'price', 'timestamp', 'active']
    list_editable = ['price', 'active']
    list_filter = ['type', 'manufacturer', 'active']
    readonly_fields = ['timestamp']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)