from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article


def index_view(request):
    articles = get_list_or_404(Article)
    context = {"articles": articles}

    return render(request, "blog/index.html", context)


def detail_view(request, id):
    article = get_object_or_404(Article, id=id)
    context = {"article": article}

    return render(request, "blog/article_detail.html", context)
