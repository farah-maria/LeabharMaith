from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('', views.all_featured, name='featured'),
]
