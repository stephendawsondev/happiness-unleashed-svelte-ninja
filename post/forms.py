from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Form for adding a new post."""
    class Meta:
        model = Post
        fields = ['image', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }
