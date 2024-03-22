from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class ActsOfKindness(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = CloudinaryField(
        'image', blank=True, null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


