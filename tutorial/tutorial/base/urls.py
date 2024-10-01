from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact-success'),
]
