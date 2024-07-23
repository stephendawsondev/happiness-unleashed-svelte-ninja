from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .models import ActsOfKindness, UserProfile, UserActStatus
from post.models import Post
from .forms import ActsOfKindnessForm
from post.forms import PostForm


@login_required
def acts_list(request):
    """Display a list of all acts of kindness."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('index'))
    acts = ActsOfKindness.objects.all()
    return render(request, 'acts_of_kindness/acts_list.html', {'acts': acts})


def act_detail(request, pk):
    """Display details of a specific act of kindness."""
    act = get_object_or_404(ActsOfKindness, pk=pk)
    return render(request, 'acts_of_kindness/act_detail.html', {'act': act})


@login_required
def add_act(request):
    """Add a new act of kindness."""
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only logged in users can do that.')
        return redirect(reverse('index'))

    def _send_confirmation_email(act):
        """Send the user a confirmation email"""
        user_email = request.user.email

        subject = render_to_string(
            'acts_of_kindness/confirmation_emails/confirmation_email_subject.txt',
            {'act': act})
        body = render_to_string(
            'acts_of_kindness/confirmation_emails/confirmation_email_body.txt',
            {'act': act, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [user_email]
        )

        messages.success(request, f'Act submitted for review! \
            You will receive an email to {user_email} confirming \
            your submission.')

    if request.method == 'POST':
        form = ActsOfKindnessForm(request.POST, request.FILES)
        if form.is_valid():
            act = form.save()
            _send_confirmation_email(act)
            return redirect(reverse('act_detail', args=[act.id]))
        else:
            messages.error(
                request, 'Failed to add act. Please ensure the form is valid and that the act is kind.')
    else:
        form = ActsOfKindnessForm()
    return render(request, 'acts_of_kindness/add_act.html', {'form': form})


@login_required
def edit_act(request, pk):
    """Edit an existing act of kindness."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('index'))
    act = get_object_or_404(ActsOfKindness, pk=pk)
    if request.method == 'POST':
        form = ActsOfKindnessForm(request.POST, request.FILES, instance=act)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated act of kindness!')
            return redirect(reverse('act_detail', args=[act.id]))
        else:
            messages.error(
                request, 'Failed to update act. Please ensure the form is valid and that the act is kind.')
    else:
        form = ActsOfKindnessForm(instance=act)
    return render(request, 'acts_of_kindness/edit_act.html', {'form': form, 'act': act})


@login_required
def delete_act(request, pk):
    """Delete an act of kindness."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('index'))
    act = get_object_or_404(ActsOfKindness, pk=pk)
    act.delete()
    messages.success(request, 'Successfully deleted act of kindness!')
    return redirect(reverse('index'))


@login_required
def complete_and_share_act(request, act_id):
    """
    Allows a user to mark an act of kindness as
    completed and decide if they want to share about it.
    """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only logged in users can do that.')
        return redirect(reverse('index'))
    user_profile = get_object_or_404(UserProfile, user=request.user)
    act_of_kindness = get_object_or_404(ActsOfKindness, pk=act_id)

    UserActStatus.objects.update_or_create(
        profile=user_profile,
        act_of_kindness=act_of_kindness,
        defaults={'completed': True}
    )

    # If the user chooses to share about the act, redirect to the add_post view in the post app
    if request.method == "POST" and 'share' in request.POST:
        return redirect('add_post', aok_pk=act_id)
    else:
        messages.success(
            request, 'Act of kindness marked as completed.', extra_tags='act_completed')
        return redirect('profile', pk=user_profile.pk)
