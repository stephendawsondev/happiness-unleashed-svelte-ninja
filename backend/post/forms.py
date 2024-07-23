from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Form for adding a new post."""
    class Meta:
        model = Post
        fields = ['image', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'I was so happy to be able to help out with this project!'}),

        }

        labels = {
            'content': 'Add your post text',
        }
