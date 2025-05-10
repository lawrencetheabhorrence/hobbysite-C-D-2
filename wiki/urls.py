from django.urls import path
from .views import ArticleListView, ArticleCreateView, ArticleDetailView

app_name = "wiki"
urlpatterns = [
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path("article/add/", ArticleCreateView.as_view(), name="article-create"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path(
        "article/<int:pk>/edit/",
        views.ArticleUpdateView.as_view(),
        name="article-update",
    ),
]