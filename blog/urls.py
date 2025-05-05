from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("articles/", views.ArticleListView.as_view(), name="article_list"),
    path("article/<int:id>", views.ArticleDetailView.as_view(), name="article_detail"),
    path("article/<int:id>/edit", views.ArticleUpdateView.as_view(), name="article_update"),
    path("article/add", views.ArticleCreateView.as_view(), name="article_create")
]
