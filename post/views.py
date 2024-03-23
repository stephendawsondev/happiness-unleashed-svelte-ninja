from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import cloudinary.uploader
import cloudinary

from profiles.models import UserProfile
from acts_of_kindness.models import ActsOfKindness, UserActStatus
from .models import Post
from .forms import PostForm


def post_detail(request, pk):
    """Display a specific post."""
    post = Post.objects.get(pk=pk)
    aok = post.act_of_kindness

    context = {
        'post': post,
        'aok': aok
    }
    return render(request, 'post/post_detail.html', context)


def post_list(request):
    """Display a list of all posts."""
    posts = Post.objects.all()

    for post in posts:
        post.aok = post.act_of_kindness

    return render(request, 'post/post_list.html', {'posts': posts})


@login_required
def add_post(request, aok_pk):
    """
    Add a new post A post can only be added by a logged in user
    and it must be related to a completed act of kindness."""

    aok = get_object_or_404(ActsOfKindness, pk=aok_pk)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_aok = get_object_or_404(UserActStatus, profile=user_profile, act_of_kindness=aok)

    if not user_aok.completed:
        messages.error(request, 'You can only add a post for a completed act of kindness.')
        return redirect('post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile = user_profile
            post.act_of_kindness = aok

            if 'image' in request.FILES:
                image = request.FILES['image']
                upload = cloudinary.uploader.upload(image)
                post.image = upload['url']

            post.save()
            messages.success(request, 'Successfully added post!')
            return redirect('profile')
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()

    context = {
        'form': form,
        'aok': aok
    }

    return render(request, 'post/add_post.html', context)

@login_required
def edit_post(request, pk):
    """Edit an existing post."""
    post = Post.objects.get(pk=pk)

    if post.user_profile.user != request.user:
        messages.error(
            request, 'You can only edit posts that you created.')
        return redirect('post_detail', pk=post.pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            if request.FILES:
                image = request.FILES['image']
                upload = cloudinary.uploader.upload(image)
                post.image = upload['url']

            post = form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('post_detail', pk=post.pk)
        else:
            messages.error(
                request, 'Failed to update post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'post/edit_post.html', context)


@login_required
def delete_post(request, pk):
    """Delete an existing post."""
    post = Post.objects.get(pk=pk)
    if post.user_profile.user != request.user:
        messages.error(
            request, 'You can only delete posts that you created.')
        return redirect('post_detail', pk=post.pk)
    post.delete()
    messages.success(request, 'Post deleted successfully')
    return redirect('profile')
