from django.shortcuts import render


def newsletter(request):
    """ A view to return the newsletter signup page """

    return render(request, 'extras/newsletter.html')
