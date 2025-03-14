from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article

def article_list(request):
    articles = get_list_or_404(Article)
    return render(request, 'wiki/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'wiki/article_detail.html', {'article': article})
