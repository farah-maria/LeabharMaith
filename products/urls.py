from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:book_id>/book_detail/', views.book_detail, name='book_detail'),
]
