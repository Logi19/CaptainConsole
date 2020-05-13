from django.urls import path, include

from .views import sign_up_view
from .views import login_view
from .views import logout_view
from .views import my_profile_view
from .views import my_profile_update

urlpatterns = [
    path('sign_up/', sign_up_view, name='sign_up_page'),
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('my_profile/', my_profile_view, name='profile_detail'),
    path('my_profile/update/', my_profile_update, name='profile_update'),
]