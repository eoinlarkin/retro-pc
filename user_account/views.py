from re import L
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

def user_account(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST': 

        # greate a new instance of the User Profile Form using the user data
        # update the form for the active user
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
             form.save()
             messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)

    # geeting the users orders
    orders = profile.orders.all()

    template = 'user_account/account.html'
    context = {
        'form': form,
        'orders': orders,

        # flag to check if on profile page; see ci video 061
        'profile_page_active': True 
    }

    return render(request, template, context) 