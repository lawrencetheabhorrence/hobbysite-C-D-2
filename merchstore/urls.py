from django.urls import path
from .views import merchstoreList, merchstoreItem

urlpatterns = [
    path('merchstore/items/', merchstoreList, name="merchstoreList"),
    path('merchstore/item/<int:num>/', merchstoreItem, name="merchstoreItem"),
    ]

#app_name = "merchstore"
