from django.urls import path, include
from .views import ArticleListView

app_name = "wiki"
urlpatterns = [
    path("articles/", ArticleListView.as_view(), name="article-list"),
]
