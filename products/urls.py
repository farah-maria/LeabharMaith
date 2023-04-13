from django.urls import path
from . import views

urlpatterns = [
     path('', views.all_products, name='products'),
     path('<int:book_id>/product_detail/', views.book_detail,
          name='book_detail'),
     path('<int:featured_id>/product_detail/', views.featured_detail,
          name='featured_detail'),
     path('add_book/', views.add_book, name='add_book'),
     path('add_featured/', views.add_featured, name='add_featured'),
     path('add_author/', views.add_author, name='add_author'),
]
