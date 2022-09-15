from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import UserProfile, NewsletterSubscribers
from .forms import UserProfileForm

from checkout.models import Order

# login required decorator
# django will check whether a user is logged in before executing the view
from django.contrib.auth.decorators import login_required


@login_required
def user_account(request):
    """Display the user's profile."""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":

        # greate a new instance of the User Profile Form using the user data
        # update the form for the active user
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Error - updated failed ! ")

    else:
        form = UserProfileForm(instance=profile)

    # geeting the users orders
    orders = profile.orders.all()

    template = "user_account/account.html"
    context = {
        "form": form,
        "orders": orders,
        # flag to check if on profile page; see ci video 061
        "profile_page_active": True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)


def newsletter_signup(request):
    """
    View to subscribe users to the website newsletter
    """
    email = request.POST["email"]
    existing_sub = NewsletterSubscribers.objects.filter(email=email).exists()
    if existing_sub:
        pass
    else:
        sub = NewsletterSubscribers(email=email)
        sub.save()
    messages.success(request, "Thank you for subscribing to our newsletter!")
    return redirect(request.GET.get("next"))
