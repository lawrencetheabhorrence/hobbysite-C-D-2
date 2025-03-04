from django.shortcuts import render
from .models import Article, ArticleCategory

def ArticleListView(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }

    return render(request, "article_list.html", context)

def ArticleDetailView(request, id):
    article = Article.objects.get(id=id)
    context = {
        "article" : article
    }

    return render(request, "article_detail.html", context)