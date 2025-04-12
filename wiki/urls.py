from django.urls import path
from . import views

app_name = "wiki"
urlpatterns = [
    path("articles/", views.article_list, name="article-list"),
    path("article/<int:pk>/", views.article_detail, name="article-detail"),
]
