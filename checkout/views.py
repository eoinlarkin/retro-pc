from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderLineItem

from store.models import Product
from user_account.models import UserProfile
from user_account.forms import UserProfileForm
from cart.contexts import cart_contents


def checkout(request):
    """
    Gets the bag from the session;
    if there is nothing in the bag it will redirect back to the product page
    """
    bag = request.session.get("cart", {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse("store"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51IdIvoH0kCl7fda6nB8HeAiTN7FpZFfb5auEu2aXR8IqdwNpZ7pRKCzVGceGpIKyykg77Tw7PZU0CFnUfFPUxfJI00glzlgyuV",
        "cient_secret": "test client secret",
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                "default_phone_number": order.phone_number,
                "default_country": order.country,
                "default_postcode": order.postcode,
                "default_town_or_city": order.town_or_city,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_county": order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(
        request,
        f"Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.",
    )

    if "cart" in request.session:
        del request.session["cart"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
