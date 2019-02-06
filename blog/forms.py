from django import forms
from .models import PostRecord

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = PostRecord
        fields = ('title', 'text')