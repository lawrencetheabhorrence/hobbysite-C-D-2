from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DetailView
from .models import Article, Comment, Image, Category
from .forms import CommentForm
# from django.contrib.auth.decorators import login_required

class ArticleListView(ListView):
    model = Article
    template_name = "wiki/article_list.html"
    context_object_name = "articles"

    # optimize queries
    def get_queryset(self):
        return Article.objects.select_related("category", "author").order_by("category__name", "title")

    def get_context_data(self, **kwargs):
        context = super().get_context(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = [ 'title', 'author', 'category', 'entry', 'header_image' ]
    template_name_suffix = '_create'

class ArticleDetailView(DetailView):
    model = Article
    template_name = "wiki/article_detail.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        
        context["related_articles"] = article.category.articles.exclude(pk=article.pk)[:2]

        context["comments"] = Comment.objects.filter(article=article).order_by('-created_on')
        
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
                comment.user = request.user
                comment.save()
                return redirect('article-detail', pk=article.pk)  
        return HttpResponse("You must be logged in to comment", status=403)
