from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Article, Comment, Image, ArticleCategory
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticleListView(ListView):
    model = Article
    template_name = "wiki/article_list.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.select_related("category", "author").order_by(
            "category__name", "title"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ArticleCategory.objects.all()
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ["title", "category", "entry", "header_image"]
    template_name_suffix = "_create"

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user.profile
        article.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ["title", "category", "entry", "header_image"]
    template_name_suffix = "_update"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context["images"] = Image.objects.filter(article=article)
        return context

    def get(self, request, *args, **kwargs):

        affected_article = get_object_or_404(Article, pk=self.kwargs["pk"])
        if request.user.profile != affected_article.author:
            return redirect(reverse_lazy("wiki:article_list"))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        affected_article = get_object_or_404(Article, pk=self.kwargs["pk"])
        if (
            request.user.is_authenticated
            and request.user.profile != affected_article.author
        ):
            return redirect(reverse_lazy("wiki:article_list"))
        return super().post(request, *args, **kwargs)


class ArticleDetailView(DetailView):
    model = Article
    template_name = "wiki/article_detail.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()

        context["related_articles"] = article.category.articles.exclude(pk=article.pk)[
            :2
        ]
        context["comments"] = Comment.objects.filter(article=article).order_by(
            "-created_on"
        )

        if self.request.user.is_authenticated:
            context["comment_form"] = CommentForm()

        context["images"] = Image.objects.filter(article=article)

        if article.author == self.request.user:
            context["edit_link"] = True

        return context

    def post(self, request, *args, **kwargs):
        article = self.get_object()

        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.article = article
                comment.author = request.user.profile
                comment.save()
                return redirect("wiki:article_detail", pk=article.pk)
        return HttpResponse("You must be logged in to comment", status=403)


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ["image", "description"]
    template_name_suffix = "_create"

    def get(self, request, *args, **kwargs):
        affected_article = get_object_or_404(Article, pk=self.kwargs["pk"])
        if request.user.profile != affected_article.author:
            return redirect(reverse_lazy("wiki:article_list"))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        print(self.kwargs)
        image = form.save(commit=False)
        image.article = Article.objects.get(pk=self.kwargs["pk"])
        image.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        affected_article = get_object_or_404(Article, pk=self.kwargs["pk"])
        if (
            request.user.is_authenticated
            and request.user.profile != affected_article.author
        ):
            return redirect(reverse_lazy("wiki:article_list"))
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return Article.objects.get(pk=self.kwargs["pk"]).get_absolute_url()


class ImageUpdateView(LoginRequiredMixin, UpdateView):
    model = Image
    fields = ["description"]
    template_name_suffix = "_update"

    def get(self, request, *args, **kwargs):
        image = self.get_object()
        if request.user.profile != image.article.author:
            return redirect(reverse_lazy("wiki:article_list"))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        image = self.get_object()
        if (
            request.user.is_authenticated
            and request.user.profile != image.article.author
        ):
            return redirect(reverse_lazy("wiki:article_list"))
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        image = self.get_object()
        return Article.objects.get(pk=image.article.pk).get_absolute_url()


class ImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image

    def get(self, request, *args, **kwargs):
        image = self.get_object()
        if request.user.profile != image.article.author:
            return redirect(reverse_lazy("wiki:article_list"))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        image = self.get_object()
        if (
            request.user.is_authenticated
            and request.user.profile != image.article.author
        ):
            return redirect(reverse_lazy("wiki:article_list"))
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        image = self.get_object()
        return Article.objects.get(pk=image.article.pk).get_absolute_url()
