from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = "blog/blog_list.html"
    context_object_name = "blog"