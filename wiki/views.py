from django.views.generic.list import ListView
from .models import Article
from collections import defaultdict 

class ArticleListView(ListView):
    model = Article
    template_name = "wiki/article_list.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.select_related("category", "author")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_articles = []
        categorized_articles = defaultdict(list)
        articles = self.get_queryset()

        if self.request.user.is_authenticated and hasattr(self.request.user, "profile"):
            user_profile = self.request.user.profile
            user_articles = articles.filter(author = user_profile)
            articles = articles.exclude(author = user_profile)

        for article in articles: 
            if article.category:
                categorized_articles[article.category.name].append(article)

        context["user_articles"] = user_articles
        context["categorized_articles"] = dict(categorized_articles)
        return context
