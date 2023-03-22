from django.contrib import admin
from .models import Book, Author, Featured_Product


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'quarter',
        'genre',
        'audience',
        'language',
        'image',
        'price',
    )

    ordering = ('quarter',)


class Featured_ProductAdmin(admin.ModelAdmin):
    list_display = (
        'quarter',
        'name',
        'manufacturer',
        'image',
        'price',
    )

    ordering = ('quarter',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Featured_Product, Featured_ProductAdmin)
