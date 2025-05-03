from django.urls import path
from . import views

app_name = "wiki"
urlpatterns = [
    path(
        "article/<int:pk>/edit/",
        views.ArticleUpdateView.as_view(),
        name="article-update",
    )
]
