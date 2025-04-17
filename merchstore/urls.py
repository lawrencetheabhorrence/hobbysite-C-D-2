from django.urls import path
from .views import productList, productDetail#, productCreate, productUpdate, cartContents, transactionList

app_name = "merchstore"
urlpatterns = [
    path("items/", productList, name="product_list"),
    path("item/<int:itemID>/", productDetail, name="product_detail"),
    #path("item/add") productCreate, name="product_create"),
    #path("item/<int:itemID>/edit", productUpdate, name="product_update"),
    #path("cart", cartContents, name="cart_contents"),
    #path("transactions", transactionList, name="transaction_list"),
]
