from django.urls import path
from . import views

app_name = "merchstore"

urlpatterns = [
    path("items/", views.ProductListView.as_view(), name="product_list"),
    path("item/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("item/add", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "item/<int:pk>/edit", views.ProductUpdateView.as_view(), name="product_update"
    ),
    path("cart/", views.CartListView.as_view(), name="cart_list"),
    path("transactions/", views.TransactionListView.as_view(), name="transaction_list"),
]
