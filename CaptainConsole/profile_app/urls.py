from django.urls import path, include

from .views import sign_up_view
from .views import login_view
from .views import logout_view
from .views import my_profile_view
from .views import my_profile_update
from .views import my_profile_search_hist
from .views import add_to_search_history

urlpatterns = [
    path('sign_up/', sign_up_view, name='sign_up_page'),
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('my_profile/', my_profile_view, name='profile_detail'),
    path('my_profile/update/', my_profile_update, name='profile_update'),
    path('my_profile/search_history/', my_profile_search_hist, name='profile_search_hist'),
    path('ajax/add_to_search_history/', add_to_search_history, name='ajax_add_to_search_history'),
]