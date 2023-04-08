from django.urls import path
from . import views

urlpatterns = [
     path('', views.all_products, name='products'),
     path('<int:book_id>/product_detail/', views.book_detail, 
          name='book_detail'),
     path('<int:featured_id>/product_detail/', views.featured_detail, 
          name='featured_detail'),
]
