from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import FrontPageView, check_out
from .views import ProductList
from .views import ProductDetail
from .views import add_to_cart


urlpatterns = [
    path('', FrontPageView.as_view(), name="frontpage"),
    path('products/', ProductList.as_view(), name="all_products"),
    path('products/<pk>/', ProductDetail.as_view(), name="product_detail"),
    path('checkout/', check_out, name="checkout"),
    #path('products/<?search=>', views.check_out, name="checkout"),
    path('ajax/add_product_to_cart/', add_to_cart, name="ajax_add_to_cart"),
]

