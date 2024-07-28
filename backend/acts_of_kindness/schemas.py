from ninja import ModelSchema
from .models import ActsOfKindness


class ActsOfKindnessSchema(ModelSchema):
    class Meta:
        model = ActsOfKindness
        fields = ('id', 'name', 'description',
                  'image', 'approved', 'user_profiles')
