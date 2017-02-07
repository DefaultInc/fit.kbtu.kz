from django import forms
from .models import Claim

class ClaimForm(forms.ModelForm):
    """
    Making a form for creating and updating views
    """
    class Meta:
        model = Claim
        fields = [
            "title",
            "reason",
            "content",
        ]