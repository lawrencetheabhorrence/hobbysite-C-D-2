from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Article, ArticleCategory


class ArticleListView(ListView):
    model = ArticleCategory
    template_name = "blog/article_list.html"
    context_object_name = "categories"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"


class ArticleCreateView(CreateView):
    model = Article
    template_name = "blog/article_create.html"
    template_name_suffix = "_create"
    fields = ["title", "category", "entry", "header_image"]


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "blog/article_update.html"
    template_name_suffix = "_update"
