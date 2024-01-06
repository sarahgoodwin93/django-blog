from .models import CollaborateRequest
from django import forms


class CollabortForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
