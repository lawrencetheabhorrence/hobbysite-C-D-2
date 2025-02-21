from django.urls import path

from . import views

urlpatterns = [
    path("threads", views.index, name="index"),
    path("thread/<int:pk>", views.thread_detail, name="thread_detail"),
]
