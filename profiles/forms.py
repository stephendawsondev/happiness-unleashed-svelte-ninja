from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class CustomUserEditForm(forms.ModelForm):
    """
    User form to output on the profile page
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address'
        }


class UserProfileForm(forms.ModelForm):
    """ Form for user profile page """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'country': 'Country',
            'bio': 'Tell us about yourself...',
        }

        labels = {
            'country': 'Country',
            'bio': 'Bio',
            'profile_image': 'Profile Image',
        }

        for field in self.fields:
            if field in placeholders:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            if field in labels:
                self.fields[field].label = labels[field]
            self.fields[field].widget.attrs['class'] = 'rounded'
