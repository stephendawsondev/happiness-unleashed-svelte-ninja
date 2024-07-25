from ninja import ModelSchema
from .models import ActsOfKindness


class ActsOfKindnessSchema(ModelSchema):

    class Meta:
        model = ActsOfKindness
        fields = ('name', 'description', 'image', 'approved', 'user_profiles')
