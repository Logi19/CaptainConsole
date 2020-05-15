from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import FrontPageView, check_out
from .views import ProductList
from .views import ProductDetail


urlpatterns = [
    path('', FrontPageView.as_view(), name="frontpage"),
    path('products/', ProductList.as_view(), name="all_products"),
    path('products/<pk>/', ProductDetail.as_view(), name="product_detail"),
    path('checkout/', check_out, name="checkout"),
]

