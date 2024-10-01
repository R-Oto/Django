from django.urls import path
from .views import register

urlpatterns = [
    path('users/', register, name='register'),  # Trailing slash here as well
]
