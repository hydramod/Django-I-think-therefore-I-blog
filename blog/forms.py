from .models import Comment
from django import forms

class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)