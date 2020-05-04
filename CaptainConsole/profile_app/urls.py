from django.urls import path

from .views import ProfileCreate
from.views import ProfileDetail
from .views import ProfileUpdate

urlpatterns = [
    path('profile/', ProfileDetail.as_view(), name='profile_detail'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
    path('profile/update/', ProfileUpdate.as_view(), name='profile_update')
]