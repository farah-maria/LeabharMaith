from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm


def about(request):
    """ A view to return the about us page """

    return render(request, 'extras/about.html')


def newsletter(request):
    """ A view to return the newsletter signup page """

    return render(request, 'extras/newsletter.html')


def privacy(request):
    """ A view to render the privacy statement in compliance with GDPR """

    return render(request, 'extras/privacy.html')


def contact(request, *args, **kwargs):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Message sent. Thank you! We will get back to you soon.'
                )
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Oops! That did not send. \
                    Check your details and try again.')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            form = ContactForm()

    return render(request, 'extras/contact.html', {'form': form})
