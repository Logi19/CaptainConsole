from django.urls import path

from .views import ReceiptView
from .views import OrderDetail
from .views import OrderCreate
from .views import remove_from_cart
from .views import my_cart
from .views import receipt_view


urlpatterns = [
    path('my_cart/', my_cart, name="cart_detail"),
    path('ajax/remove_item/', remove_from_cart, name='remove_from_cart'),
    path('order/create/', OrderCreate.as_view(), name='order_create'),
    path('order/<pk>/', OrderDetail.as_view(), name='order_detail'),
    path('receipt/', receipt_view, name='receipt_view')
]
