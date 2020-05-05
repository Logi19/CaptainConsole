from django.urls import path

from .views import FrontPageView
from .views import ProductList
from .views import ProductDetail

urlpatterns = [
    path('products/', ProductList.as_view(), name="product_list"),
    path('products/<pk>/', ProductDetail.as_view(), name="product_detail"),
]
