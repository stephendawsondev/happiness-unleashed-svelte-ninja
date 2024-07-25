from django.db import models
from cloudinary.models import CloudinaryField
from profiles.models import UserProfile


class ActsOfKindness(models.Model):
    name: str = models.CharField(max_length=254)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    approved: bool = models.BooleanField(default=False)
    user_profiles = models.ManyToManyField(
        UserProfile, through='UserActStatus', related_name="acts_of_kindness")

    def __str__(self):
        return self.name


class UserActStatus(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    act_of_kindness = models.ForeignKey(
        ActsOfKindness, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('profile', 'act_of_kindness')
