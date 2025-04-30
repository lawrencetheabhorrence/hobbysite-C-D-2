from django.views.generic.list import ListView
from .models import Article, Category

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
