from django.urls import path

from . import views

app_name = "user_management"
urlpatterns = [
    path("", views.update, name="update"),
]
