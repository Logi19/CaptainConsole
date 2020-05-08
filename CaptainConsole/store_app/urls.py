from django.urls import path

from .views import FrontPageView
from .views import ProductList
from .views import ProductDetail
from .views import single_product
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', FrontPageView.as_view(), name="frontpage"),
    path('products/', ProductList.as_view(), name="all_products"),
    path('products/<int:id>/', single_product, name="product_detail"),
]

