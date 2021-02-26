from django.db.models import fields
from .models import Post,Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','text','auther']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text','author']