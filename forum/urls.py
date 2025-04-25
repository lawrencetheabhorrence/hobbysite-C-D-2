from django.urls import path
from .views import ThreadList, ThreadDetail, ThreadCreate, ThreadUpdate


app_name = "forum"
urlpatterns = [
    path("threads/", ThreadList.as_view(), name="index"),
    path("thread/<int:pk>/", ThreadDetail.as_view(), name="detail"),
    path("thread/add/", ThreadCreate.as_view(), name="thread_create"),
    path("thread/<int:pk>/edit/", ThreadUpdate.as_view(), name="thread_update"),
]
