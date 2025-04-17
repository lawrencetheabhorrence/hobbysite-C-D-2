from django.views.generic.list import ListView
from .models import Article 

class ArticleListView(ListView):
    model = Article
    template_name = "wiki/article_list.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.select_related("category", "author")
    