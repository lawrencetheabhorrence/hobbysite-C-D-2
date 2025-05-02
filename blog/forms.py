from .models import Comment, Article, ArticleCategory
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "entry"


class ArticleForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=ArticleCategory.objects.all(),
        empty_label="Select a category",
    )

    class Meta:
        model = Article
        fields = ("title", "category", "entry", "header_image")


class ArticleUpdateForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=ArticleCategory.objects.all(),
        empty_label="Select a category",
    )

    class Meta:
        model = Article
        fields = ("title", "category", "entry", "header_image")
