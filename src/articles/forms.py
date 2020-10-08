from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]

    comment = forms.CharField(label='', widget=forms.Textarea(attrs = {'rows': 3, 'cols': 36}))