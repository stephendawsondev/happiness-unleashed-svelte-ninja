from ninja import Schema
from .models import Post
from datetime import datetime


class PostSchema(Schema):
    act_of_kindness_id: int
    user_profile_id: int
    created_at: datetime
    updated_at: datetime
    content: str
    image_url: str  # Directly name the field as expected in the response

    @classmethod
    def from_django(cls, obj):
        """Method to convert Django model instance to Pydantic model instance."""
        return cls(
            act_of_kindness_id=obj.act_of_kindness.id,
            user_profile_id=obj.user_profile.id,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
            content=obj.content,
            image_url=obj.image.url if obj.image else None
        )
