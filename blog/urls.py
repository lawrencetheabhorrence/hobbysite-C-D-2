from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("articles", views.index_view, name="index"),
    path("article/<int:id>", views.detail_view, name="thread_detail"),
]