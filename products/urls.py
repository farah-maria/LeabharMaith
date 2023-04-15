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
     path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
     path('edit_featured/<int:featured_id>/', views.edit_featured,
          name='edit_featured'),
     path('edit_author/<int:author_id>/', views.edit_author,
          name='edit_author'),
     path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
     path('delete_featured/<int:featured_id>/', views.delete_featured,
          name='delete_featured'),
     path('delete_author/<int:author_id>/', views.delete_author,
          name='delete_author'),
]
