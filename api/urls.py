from django.urls import path, re_path
from .views import get_users, create_user, manipulate_user, get_users_by_search

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('user/<int:pk>', manipulate_user, name='manipulate_user'),
    re_path('^users/search/(?P<search>.+)$', get_users_by_search, name='get_users_by_search'),
]