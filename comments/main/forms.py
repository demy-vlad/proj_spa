from django import forms
from .models import CommentForm

class ReplyForm(forms.ModelForm):
    class Meta:
        model = CommentForm
        fields = ['user_name', 'email', 'text']

class CommentFormForm(forms.ModelForm):
    class Meta:
        model = CommentForm
        fields = ['user_name', 'email', 'home_page', 'text', 'parent_comment', 'file']