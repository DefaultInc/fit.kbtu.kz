from django import forms
from .models import Post, Comment


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


class CommentForm(forms.ModelForm):
    """
    Making a form for creating a comment
    """

    class Meta:
        model = Comment
        fields = [
            "content",
        ]
