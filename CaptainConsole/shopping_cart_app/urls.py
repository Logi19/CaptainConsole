from django.urls import path

from .views import ShoppingCartDetail
from .views import ReceiptView
from .views import OrderDetail
from .views import OrderCreate
from .views import remove_from_cart

urlpatterns = [
    path('<pk>/', ShoppingCartDetail.as_view(), name='shoppingcart_detail'),
    path('delete/<product_id>/<cart_id>/', remove_from_cart, name='remove_from_cart'),
    path('order/create/', OrderCreate.as_view(), name='order_create'),
    path('order/<pk>/', OrderDetail.as_view(), name='order_detail'),
    path('receipt/', ReceiptView.as_view(), name='receipt_view')
]
