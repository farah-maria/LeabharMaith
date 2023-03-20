from django.shortcuts import render
from .models import Book, Featured_Product


def all_books(request):
    """A view to return the products pages, incl sorting & search queries"""
    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'products/products.html', context)


def all_featured(request):
    """A view to return the products pages, incl sorting & search queries"""
    featured = Featured_Product.objects.all()

    context = {
        'featured': featured,
    }

    return render(request, 'products/products.html', context)
