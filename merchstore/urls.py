from django.urls import path
from .views import merchstoreList, merchstoreItem

app_name = "merchstore"
urlpatterns = [
    path("items/", merchstoreList, name="merchstore_list"),
    path("item/<int:itemID>/", merchstoreItem, name="merchstore_item"),
]
