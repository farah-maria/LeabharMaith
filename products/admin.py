from django.contrib import admin
from .models import Book, Author, Featured_Product


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Featured_Product)
