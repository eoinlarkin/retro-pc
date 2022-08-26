from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm

def user_account(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)

    # geeting the users orders
    orders = profile.orders.all()

    template = 'user_account/account.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context) 