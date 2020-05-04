from django.urls import path

from .views import ShoppingCartDetail
from .views import ReceiptView
from .views import OrderDetail
from .views import OrderCreate

urlpatterns = [
    path('', ShoppingCartDetail.as_view(), name='shopping_cart_detail'),
    path('order/create/', OrderCreate.as_view(), name='order_create'),
    path('order/<pk>/', OrderDetail.as_view(), name='order_detail'),
    path('receipt/', ReceiptView.as_view(), name='receipt_view')
]
