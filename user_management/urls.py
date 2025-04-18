from django.urls import path

from . import views

app_name = "user_management"
urlpatterns = [
    path("update/", views.update, name="update"),
    path("register/", views.ProfileCreateView.as_view(), name="register"),
]
