from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
]
