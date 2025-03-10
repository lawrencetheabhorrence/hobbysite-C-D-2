from django.urls import path
from .views import merchstoreList, merchstoreEntry

urlpatterns = [
    path('merchstore/items/', merchstoreList, name="merchstoreList"),
    path('merchstore/item/<int:num>/', merchstoreItem, name="merchstoreItem"),
    ]
