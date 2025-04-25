from django.urls import path
from .views import ThreadListView, ThreadDetailView, ThreadCreate, ThreadUpdate


app_name = "forum"
urlpatterns = [
    path("threads/", ThreadListView.as_view(), name="index"),
    path("thread/<int:pk>/", ThreadDetailView.as_view(), name="detail"),
    path("thread/add/", ThreadCreate.as_view(), name="thread_create"),
    path("thread/<int:pk>/edit/", ThreadUpdate.as_view(), name="thread_update"),
]
