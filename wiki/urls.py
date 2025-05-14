from django.urls import path
from .views import (
    ArticleListView,
    ArticleCreateView,
    ArticleDetailView,
    ArticleUpdateView,
    ImageCreateView,
    ImageUpdateView,
    ImageDeleteView,
)

app_name = "wiki"
urlpatterns = [
    path("articles/", ArticleListView.as_view(), name="article_list"),
    path("article/add/", ArticleCreateView.as_view(), name="article_create"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path(
        "article/<int:pk>/edit/",
        ArticleUpdateView.as_view(),
        name="article_update",
    ),
    path("article/<int:pk>/image/add/", ImageCreateView.as_view(), name="image_create"),
    path("image/<int:pk>/edit/", ImageUpdateView.as_view(), name="image_update"),
    path("image/<int:pk>/delete/", ImageDeleteView.as_view(), name="image_delete"),
]
