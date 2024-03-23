from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import cloudinary.uploader
import cloudinary
from django.shortcuts import get_object_or_404

from .models import UserProfile
from acts_of_kindness.models import ActsOfKindness, UserActStatus

from .forms import UserProfileForm, CustomUserEditForm


@login_required
def profile(request):
    """ Display the user's profile."""
    profile = get_object_or_404(UserProfile, user=request.user)
    user_form = CustomUserEditForm(instance=request.user)
    form = UserProfileForm(instance=profile)

    completed_acts = UserActStatus.objects.filter(profile=profile, completed=True, act_of_kindness__isnull=False)
    
    if request.method == 'POST':
        user_form = CustomUserEditForm(request.POST, instance=request.user)
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and form.is_valid():
            user_form.save()
            profile_form = form.save(commit=False)
            if 'profile_image' in request.FILES:
                profile_form.profile_image = request.FILES['profile_image']
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')

    context = {
        'user_form': user_form,
        'form': form,
        'profile': profile,
        'completed_acts': completed_acts
    }
    return render(request, 'profiles/profile.html', context)


@login_required
def account_delete(request):
    """ Deletes the profile's account and logs them out."""
    if request.method == 'POST':
        profile = request.profile
        profile.delete()
        logout(request)
        messages.success(
            request, 'Your account has been successfully deleted.')
        return redirect(reverse('index'))
    else:
        return redirect(reverse('profile'))
