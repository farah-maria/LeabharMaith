from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Book, Author, Featured_Product
from .forms import BookForm, FeaturedForm, AuthorForm


def all_products(request):
    """A view to return the products pages, incl sorting & search queries"""
    books = Book.objects.all()
    featured_products = Featured_Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))

        queries = Q(title__icontains=query) | Q(blurb__icontains=query)
        books = books.filter(queries)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            
        if 'category' in request.GET:
            friendly_name = request.GET['category'].split(',')[0]
            books = books.filter(category__friendly_name=friendly_name)

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
    """ A view to show individual featured product details """

    featured = get_object_or_404(Featured_Product, pk=featured_id)

    context = {
        'featured': featured_product,
    }

    return render(request, 'products/product_detail.html', context)


def add_book(request):
    """ Add a book to the shop - for shop owners """
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added book!')
            return redirect(reverse('add_book'))
        else:
            messages.error(request,
                           'Failed to add book. Please ensure input is valid.')
    else:
        form = BookForm()

    template = 'products/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def add_author(request):
    """ Add an author to the system - for shop owners """
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added writer!')
            return redirect(reverse('add_author'))
        else:
            messages.error(request,
                           'Failed to add. Please ensure input is valid.')
    else:
        form = AuthorForm()

    template = 'products/add_author.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def add_featured(request):
    """ Add a featured product to the shop - for shop owners """
    if request.method == 'POST':
        form = FeaturedForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_featured'))
        else:
            messages.error(request,
                           'Failed to add. Please ensure input is valid.')
    else:
        form = FeaturedForm()

    template = 'products/add_featured.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
