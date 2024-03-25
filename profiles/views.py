from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import logout
import cloudinary.uploader
import cloudinary

from .models import UserProfile
from acts_of_kindness.models import ActsOfKindness, UserActStatus

from .forms import UserProfileForm, CustomUserEditForm


def profile(request, pk):
    """ Display the user's profile."""
    profile = get_object_or_404(UserProfile, pk=pk)

    is_profile_owner = request.user.is_authenticated and request.user.id == profile.user.id

    if is_profile_owner:
        user_form = CustomUserEditForm(instance=request.user)
        form = UserProfileForm(instance=profile)
    else:
        user_form = None
        form = None

    completed_acts = UserActStatus.objects.filter(
        profile=profile, completed=True, act_of_kindness__isnull=False)

    if is_profile_owner and request.method == 'POST':
        user_form = CustomUserEditForm(request.POST, instance=request.user)
        form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and form.is_valid():
            if 'profile_image' in request.FILES:
                image = request.FILES['profile_image']
                upload = cloudinary.uploader.upload(image)
                form.instance.profile_image = upload['url']

            user_form.save()
            profile_form = form.save(commit=False)
            if 'profile_image' in request.FILES:
                profile_form.profile_image = request.FILES['profile_image']
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile', pk=pk)
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')

    context = {
        'is_profile_owner': is_profile_owner,
        'user_form': user_form,
        'form': form,
        'profile': profile,
        'completed_acts': completed_acts,
    }
    return render(request, 'profiles/profile.html', context)


@login_required
def account_delete(request):
    """ Deletes the profile's account and logs them out."""
    if request.method == 'POST':
        profile = request.user.userprofile
        profile.delete()
        logout(request)
        messages.success(
            request, 'Your account has been successfully deleted.')
        return redirect(reverse('index'))
    else:
        return redirect(reverse('profile'))
