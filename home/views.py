from django.shortcuts import render

# Create your views here.


def index(request):
    """A view to return the index page"""

    return render(request, 'home/index.html')


def newsletter(request):
    """a view to return the newsletter signup page"""

    return render(request, 'home/newsletter.html')
