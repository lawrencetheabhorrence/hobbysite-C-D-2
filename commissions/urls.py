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
    path(
        "<int:pk>/edit/", views.CommissionUpdateView.as_view(), name="update_commission"
    ),
    path("job/<int:pk>", views.JobView.as_view(), name="job_view"),
]
