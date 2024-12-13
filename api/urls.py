from django.urls import path, re_path
from .views import get_users, create_user, manipulate_user, get_users_by_search, get_addresses, create_address

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('user/<int:pk>', manipulate_user, name='manipulate_user'),
    path('addresses/', get_addresses, name='get_addresses'),
    path('address/create/', create_address, name='create_address'),
    re_path('^users/search/(?P<search>.+)$', get_users_by_search, name='get_users_by_search'),
]