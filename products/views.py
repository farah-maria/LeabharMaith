from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Book, Author, Featured_Product


def all_products(request):
    """A view to return the products pages, incl sorting & search queries"""
    books = Book.objects.all()
    featured_products = Featured_Product.objects.all()

    context = {
        'books': books,
        'featured_products': featured_products,
    }

    return render(request, 'products/products.html', context)


def book_detail(request, book_id):
    """ A view to show individual book details """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'products/book_detail.html', context)
