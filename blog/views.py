from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "blogs"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "blogs"
