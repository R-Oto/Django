from .views import *
from django.urls import path
from .models import *

urlpatterns = [
    path('', index, name='index'),
]
