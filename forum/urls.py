from django.urls import path

from . import views

app_name = "forum"
urlpatterns = [
    path("threads", views.IndexView.as_view(), name="index"),
    path("thread/<int:pk>", views.PostDetailView.as_view(), name="thread_detail"),
]
