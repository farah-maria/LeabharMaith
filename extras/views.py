from django.shortcuts import render


def about(request):
    """ A view to return the about us page """

    return render(request, 'extras/about.html')


def newsletter(request):
    """ A view to return the newsletter signup page """

    return render(request, 'extras/newsletter.html')
