from django.urls import path
from . import views

urlpatterns = [
     path('', views.all_products, name='products'),
     path('<int:book_id>/product_detail/', views.book_detail, 
          name='book_detail'),
     path('<int:featured_id>/product_detail/', views.featured_detail, 
          name='featured_detail'),
     path('admin/', admin.site.urls),
     path('accounts/', include('allauth.urls')),
     path('', include('home.urls')),
     path('products/', include('products.urls')),
     path('basket/', include('basket.urls')),
     path('checkout/', include('checkout.urls')),
     path('profile/', include('profiles.urls')),
]
