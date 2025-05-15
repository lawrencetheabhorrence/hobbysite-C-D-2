from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Article, ArticleCategory, Comment
from .forms import CommentForm


class ArticleListView(ListView):
    model = ArticleCategory
    template_name = "blog/article_list.html"
    context_object_name = "categories"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()

        context["related_articles"] = (
            Article.objects.all()
            .exclude(pk=article.pk)
            .filter(author=article.author)[:2]
        )

        context["comments"] = Comment.objects.filter(article=article).order_by(
            "-created_on"
        )

        return context

    def post(self, request, *args, **kwargs):
        article = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user.profile
            comment.save()

        return redirect("blog:article_detail", pk=article.pk)


class ArticleCreateView(CreateView):
    model = Article
    template_name_suffix = "_create"
    fields = ["title", "category", "entry", "header_image"]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        return redirect(reverse("blog:article_list"))

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user.profile
        article.save()
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    template_name_suffix = "_update"
    fields = ["title", "category", "entry", "header_image"]

    def get(self, request, *args, **kwargs):
        affected_article = get_object_or_404(Article, pk=self.kwargs["pk"])
        if (
            request.user.is_authenticated
            and request.user.profile != affected_article.author
        ):
            return redirect(reverse_lazy("blog:article_list"))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        return redirect(reverse("blog:article_list"))
