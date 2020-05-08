from django.urls import path, include

from .views import ProfileCreate
from .views import ProfileDetail
from .views import ProfileUpdate

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('<pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('create/', ProfileCreate.as_view(), name='profile_create'),
    path('update/', ProfileUpdate.as_view(), name='profile_update')
]