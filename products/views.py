from django.shortcuts import render
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


def product_detail(request):
    """ A view to show individual product details """

    book = get_object_or_404(Book)
    featured_product = get_object_or_404(Featured_Product)

    context = {
        'book': book,
        'featured_product': featured_product,
    }

    return render(request, 'products/product_detail.html', context)
