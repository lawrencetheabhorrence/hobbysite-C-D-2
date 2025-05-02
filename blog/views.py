from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Article
from .forms import CommentForm, ArticleForm, ArticleUpdateForm


class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "blogs"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context


class ArticleCreateView(CreateView):
    model = Article
    template_name = "blog/article_create_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_form"] = ArticleForm()
        return context


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "blog/article_update_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_form"] = ArticleUpdateForm()
        return context
