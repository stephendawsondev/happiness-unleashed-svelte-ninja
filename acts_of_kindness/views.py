from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ActsOfKindness, UserProfile, UserActStatus
from .forms import ActsOfKindnessForm

#@login_required
def acts_list(request):
    """Display a list of all acts of kindness."""
    acts = ActsOfKindness.objects.all()
    return render(request, 'acts_of_kindness/acts_list.html', {'acts': acts})


def act_detail(request, pk):
    """Display details of a specific act of kindness."""
    act = get_object_or_404(ActsOfKindness, pk=pk)
    return render(request, 'acts_of_kindness/act_detail.html', {'act': act})


#@login_required
def add_act(request):
    """Add a new act of kindness."""
    #if not request.user.is_authenticated:
     #   messages.error(request, 'Sorry, only logged in users can do that.')
      #  return redirect(reverse('index'))
    if request.method == 'POST':
        form = ActsOfKindnessForm(request.POST, request.FILES)
        if form.is_valid():
            act = form.save()
            messages.success(request, 'Successfully added act of kindness! Admin will approve and publish the act as soon as possible')
            return redirect(reverse('act_detail', args=[act.id]))
        else:
            messages.error(request, 'Failed to add act. Please ensure the form is valid and that the act is kind.')
    else:
        form = ActsOfKindnessForm()
    return render(request, 'acts_of_kindness/add_act.html', {'form': form})


#@login_required
def edit_act(request, pk):
    """Edit an existing act of kindness."""
    #if not request.user.is_superuser:
     #   messages.error(request, 'Sorry, only admin can do that.')
      #  return redirect(reverse('index'))
    act = get_object_or_404(ActsOfKindness, pk=pk)
    if request.method == 'POST':
        form = ActsOfKindnessForm(request.POST, request.FILES, instance=act)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated act of kindness!')
            return redirect(reverse('act_detail', args=[act.id]))
        else:
            messages.error(request, 'Failed to update act. Please ensure the form is valid and that the act is kind.')
    else:
        form = ActsOfKindnessForm(instance=act)
    return render(request, 'acts_of_kindness/edit_act.html', {'form': form, 'act': act})


#@login_required
def delete_act(request, pk):
    """Delete an act of kindness."""
    #if not request.user.is_superuser:
     #   messages.error(request, 'Sorry, only admin can do that.')
      #  return redirect(reverse('index'))
    act = get_object_or_404(ActsOfKindness, pk=pk)
    act.delete()
    messages.success(request, 'Successfully deleted act of kindness!')
    return redirect(reverse('index'))

#@login_required
def completed_act(request, act_id):
    #if not request.user.is_authenticated:
     #   messages.error(request, 'Sorry, only logged in users can do that.')
      #  return redirect(reverse('index'))
     if request.method == "POST":
        user_profile = request.user.userprofile
        act_of_kindness = get_object_or_404(ActsOfKindness, pk=act_id)

        UserActStatus.objects.update_or_create(
            user_profile=user_profile,
            act_of_kindness=act_of_kindness,
            defaults={'completed': True}
        )
        messages.success(request, 'Great job doing an act of kindness!')
        return redirect('profiles:profile')


