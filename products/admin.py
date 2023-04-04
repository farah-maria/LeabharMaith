from django.contrib import admin
from .models import Category, Book, Author, Featured_Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'genre',
    )


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'quarter',
        'genre',
        'category',
        'audience',
        'title',
        'author',
        'language',
        'featured_image',
        'price',
        'in_stock',
    )

    ordering = ('quarter',)


class Featured_ProductAdmin(admin.ModelAdmin):
    list_display = (
        'quarter',
        'name',
        'manufacturer',
        'featured_image',
        'price',
        'in_stock',
    )

    ordering = ('quarter',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Featured_Product, Featured_ProductAdmin)
