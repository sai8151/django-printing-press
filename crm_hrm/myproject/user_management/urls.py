# user_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('user-list/', views.user_list, name='user_list'),
    path('create-user/', views.create_user, name='create_user'),
]
