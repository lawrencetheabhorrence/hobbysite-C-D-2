from django.urls import path
from . import views

app_name = "commissions"

urlpatterns = [
    path("list/", views.CommissionListView.as_view(), name="commission_list"),
    path(
        "detail/<int:commission_id>/", views.commission_detail, name="commission_detail"
    ),
    path("add/", views.CommissionCreateView.as_view(), name="add_commission"),
]
