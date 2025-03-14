from django.urls import path
from .views import merchstoreList, merchstoreVariety, merchstoreItem

urlpatterns = [
    path("items/", merchstoreList, name="merchstore_list"),
    path("items/<str:product_type>", merchstoreVariety, name="merchstore_variety"),
    path("item/<int:itemID>/", merchstoreItem, name="merchstore_item"),
    ]
