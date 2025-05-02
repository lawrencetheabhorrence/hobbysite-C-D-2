from django.urls import path
from . import views
from .views import productCreate

app_name = "merchstore"

urlpatterns = [
    path("items/", views.ProductListView.as_view(), name="product_list"),
    path("item/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("item/add", productCreate, name="product_create"),
    # path("item/<int:itemID>/edit", productUpdate, name="product_update"),
    # path("cart", cartContents, name="cart_contents"),
    # path("transactions", transactionList, name="transaction_list"),
]
