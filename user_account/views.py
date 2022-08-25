from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def user_account(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'user_account/account.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)