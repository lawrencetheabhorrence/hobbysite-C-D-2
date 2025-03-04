from django.shortcuts import render
from .models import Article, ArticleCategory

def index_view(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }

    return render(request, "blog/index.html", context)

def detail_view(request, id):
    article = Article.objects.get(id=id)
    context = {
        "article" : article
    }

    return render(request, "blog/article_detail.html", context)