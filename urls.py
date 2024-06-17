# accounts/urls.py

from django.urls import path
from .views import create_superuser

urlpatterns = [
    path('create_superuser/', create_superuser, name='create_superuser'),
]
