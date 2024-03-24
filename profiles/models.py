from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    Profile for user with information on things like
    address, phone number, etc.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_image = CloudinaryField(
        'image', blank=True, null=True,
        default=(
            "https://res.cloudinary.com/dyoueyepq/image/"
            "upload/v1694389081/default_profile_ekdors.jpg"
            )
        )
    country = CountryField(blank_label='Country',
                           null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
