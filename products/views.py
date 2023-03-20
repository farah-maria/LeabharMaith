from django.shortcuts import render
from .models import Book, Featured_Product


def all_products(request):
    """A view to return the products pages, incl sorting & search queries"""
    books = Book.objects.all()
    featured_products = Featured_Product.objects.all()

    context = {
        'books': books,
        'featured_products': featured_products,
    }

    return render(request, 'products/products.html', context)
