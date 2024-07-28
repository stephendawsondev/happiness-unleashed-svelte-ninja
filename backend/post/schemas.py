from ninja import ModelSchema
from .models import Post
from profiles.schemas import UserProfileSchema


class PostSchema(ModelSchema):
    user_profile: UserProfileSchema | None = None

    class Meta:
        model = Post

        fields = ['act_of_kindness', 'user_profile',
                  'created_at', 'updated_at', 'content', 'image']
