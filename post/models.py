from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

from acts_of_kindness.models import ActsOfKindness
from profiles.models import UserProfile


class Post(models.Model):
    """ Model for user-created posts."""
    act_of_kindness = models.ForeignKey(
        ActsOfKindness, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return f'{self.user_profile.user.username} - {self.act_of_kindness.name}'

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
