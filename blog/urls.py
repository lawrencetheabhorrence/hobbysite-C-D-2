from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("articles/", views.ArticleListView, name="article_list"),
    path("article/<int:id>", views.ArticleDetailView, name="article_detail"),
    path("article/<int:id>/edit", views.ArticleUpdateView, name="article_update"),
    path("article/add", views.ArticleCreateView, name="article_create")
]
