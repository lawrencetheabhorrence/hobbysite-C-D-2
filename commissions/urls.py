from django.urls import path
from . import views

app_name = "commissions"

urlpatterns = [
    path("list/", views.CommissionListView.as_view(), name="commission_list"),
    path(
        "detail/<int:pk>/",
        views.CommissionDetailView.as_view(),
        name="commission_detail",
    ),
]
