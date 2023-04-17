from django.shortcuts import render
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
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            subject = form.cleaned_data['subject'],
            message = form.cleaned_data['message'],
            form.save()

            send_mail({subject}, f'{name}, {email}, {message}',
                      settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],
                      fail_silently=False)
            messages.success(request,
                             f'Message sent.'
                             f'Thank you! We will get back to you soon.')

            return redirect(reverse('products'))
        else:
            messages.error(request,
                           f'Oops, that did not work.'
                           f'Check that your input is valid.'
                           )

    else:
        form = ContactForm()

    return render(request, 'extras/contact.html', {'form': form})
