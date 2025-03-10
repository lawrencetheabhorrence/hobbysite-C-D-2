from django.urls import path
from . import views

app_name = "commissions"

urlpatterns = [
    path("list/", views.commission_list, name="commission_list"),
    path("detail/<int:commission_id>/", views.commission_detail, name="commission_detail"),
]
