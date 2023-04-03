from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Book, Author, Featured_Product


def all_products(request):
    """A view to return the products pages, incl sorting & search queries"""
    books = Book.objects.all()
    featured_products = Featured_Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('books'))

            queries = Q(title__icontains=query) | Q(blurb__icontains=query)
            books = books.filter(queries)

    context = {
        'books': books,
        'featured_products': featured_products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def book_detail(request, book_id):
    """ A view to show individual book details """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'products/product_detail.html', context)


def featured_detail(request, featured_id):
    """ A view to show individual book details """

    featured = get_object_or_404(Featured_Product, pk=featured_id)

    context = {
        'featured': featured_product,
    }

    return render(request, 'products/product_detail.html', context)


    

