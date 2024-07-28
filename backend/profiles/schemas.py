from ninja import ModelSchema
from django.contrib.auth.models import User
from .models import UserProfile


class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserProfileSchema(ModelSchema):
    user: UserSchema | None = None

    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'profile_image']
