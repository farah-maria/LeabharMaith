from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    basket_items = []
    total = 0
    book_count = 0

    free_delivery_threshold = settings.FREE_DELIVERY_THRESHOLD

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    free_featured_product_threshold = settings.FREE_FEATURED_PRODUCT_THRESHOLD

    if total < settings.FREE_FEATURED_PRODUCT_THRESHOLD:
        featured_product = 0
    else:
        featured_product = 1

    grand_total = delivery + total

    context = {

        'basket_items': basket_items,
        'total': total,
        'book_count': book_count,
        'delivery': delivery,
        'featured_product': featured_product,
        'free_featured_product_threshold': free_featured_product_threshold,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': free_delivery_threshold,
        'grand_total': grand_total,
    }

    return context
