from django.urls import path
from .views import get_users, create_user, manipulate_user

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('user/<int:pk>', manipulate_user, name='manipulate_user'),
]