# contexts
# purpose is to make the context dictionary availalbe across the application
# this needs to be added to the contexts processor in settings.py

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from store.models import Product

from retropc.settings import FREE_DELIVERY_THRESHOLD

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
        })


    if total < settings.FREE_DELIVERY_THRESHOLD:
            delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
            free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
            delivery = 0
            free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context