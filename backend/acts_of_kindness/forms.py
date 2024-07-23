from django import forms
from .models import ActsOfKindness

class ActsOfKindnessForm(forms.ModelForm):
    class Meta:
        model = ActsOfKindness
        fields = ['name', 'description', 'image']
        labels = {
            'name': 'Name',
            'description': 'Description',
            'image': 'Image',
        }