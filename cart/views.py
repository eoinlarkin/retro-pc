from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from store.models import Product


def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """
    Add a quantity of the specified product to the shopping cart
    """

    product = Product.objects.get(pk=item_id)

    # This quantity value is coming from the form
    # We will need to convert it to an integer as it is being read in as a string
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")

    # if there is a cart dictionary in the current session we use that
    # otherwise we create an empty dictionary for this value
    cart = request.session.get("cart", {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f"Added {product.name} to your bag")
    else:
        cart[item_id] = quantity
        messages.success(request, f"Added {product.name} to your bag")
        print('message printed')

    request.session["cart"] = cart
    print(cart)
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    """

    quantity = int(request.POST.get("quantity"))

    # if there is a cart dictionary in the current session we use that
    # otherwise we create an empty dictionary for this value
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session["cart"] = cart
    return redirect(reverse("cart"))


def increase_cart_quantity(request, item_id):
    """
    Increase the quantity of the selected item by 1
    """

    quantity = int(request.POST.get("quantity"))

    # if there is a cart dictionary in the current session we use that
    # otherwise we create an empty dictionary for this value
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[item_id] = quantity +1
    else:
        cart.pop(item_id)

    request.session["cart"] = cart
    return redirect(reverse("view_cart"))



def remove_from_cart(request, item_id):
    """
    Remove the item from the shopping cart
    """
    try:
        # if there is a cart dictionary in the current session we use that
        # otherwise we create an empty dictionary for this value
        cart = request.session.get("cart", {})

        cart.pop(item_id)

        request.session["cart"] = cart
        return HttpResponse(status=200)
    except Exception:
        return HttpResponse(status=500)
