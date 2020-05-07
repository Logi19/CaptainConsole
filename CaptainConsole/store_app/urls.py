from django.urls import path

from .views import FrontPageView
from .views import ProductList
from .views import ProductDetail
from .views import all_products
from .views import single_product
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', FrontPageView.as_view(), name="frontpage"),
    path('products/', all_products , name="all_products"),
    path('products/<int:id>/', single_product, name="product_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

