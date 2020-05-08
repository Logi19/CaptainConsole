from django.urls import path, include

from .views import ProfileDetail
from .views import ProfileUpdate
from .views import sign_up_view
from .views import login_view
from .views import logout_view

urlpatterns = [
    path('sign_up/', sign_up_view, name='sign_up_page'),
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('<int:id>/', ProfileDetail.as_view(), name='profile_detail'),
    path('update/', ProfileUpdate.as_view(), name='profile_update')
]