from django.urls import path
from . import views


app_name = "forum"
urlpatterns = [
    path("threads/", views.thread_list, name="index"),
    path("thread/<int:pk>/", views.detail_view, name="thread_detail"),

    path('thread/add/', views.thread_create, name='thread_create'),
    path('thread/<int:pk>/edit/', views.thread_update, name='thread_update'),
]