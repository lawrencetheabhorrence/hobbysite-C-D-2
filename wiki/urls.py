from django.urls import path, include
from .views import ArticleListView, ArticleCreateView

app_name = "wiki"
urlpatterns = [
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path('article/add/', ArticleCreateView.as_view(), name='article-create')
]