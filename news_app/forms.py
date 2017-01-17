from django import forms
from .models import Post
from .models import Comments

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


class CommentsForm(forms.ModelForm):
    """
    Making a form for creating a comment
    """
    class Meta:
        model = Comments
        fields = [
            "comment_content",
        ]
