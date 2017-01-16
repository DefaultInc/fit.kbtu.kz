from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Making a form for creating and updating views
    """
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
        ]
