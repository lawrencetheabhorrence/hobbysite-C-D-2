from django.urls import path
from . import views

app_name = "wiki"
urlpatterns = [
    path("article/<int:pk>/", views.article_detail, name="article-detail"),
]
