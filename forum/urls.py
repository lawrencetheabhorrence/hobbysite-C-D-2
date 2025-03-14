from django.urls import path

from . import views

app_name = "forum"
urlpatterns = [
    path("threads", views.index_view, name="index"),
    path("thread/<int:pk>", views.detail_view, name="thread_detail"),
]
