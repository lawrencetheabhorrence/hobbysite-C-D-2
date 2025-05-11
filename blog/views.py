from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Article, ArticleCategory
from .forms import CommentForm


class ArticleListView(ListView):
    model = ArticleCategory
    template_name = "blog/article_list.html"
    context_object_name = "categories"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"

    def post(self, request, *args, **kwargs):
        article = self.get_object()

        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.article = article
                comment.author = request.user.profile
                comment.save()
                return redirect("blog:article_detail", pk=article.pk)
        return HttpResponse("You must be logged in to comment", status=403)


class ArticleCreateView(CreateView):
    model = Article
    template_name = "blog/article_create.html"
    template_name_suffix = "_create"
    success_url = reverse_lazy("blog:article_list")
    fields = ["title", "category", "entry", "header_image"]

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user.profile
        article.save()
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "blog/article_update.html"
    template_name_suffix = "_update"
    success_url = reverse_lazy("blog:article_list")
    fields = ["title", "category", "entry", "header_image"]
