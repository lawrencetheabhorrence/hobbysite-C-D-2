from .models import Comment, Article
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('entry')

class ArticleForm():
    class Meta:
        model = Article
        fields = ('title', 'category', 'entry', 'header_image')