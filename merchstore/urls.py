from django.urls import path
from .views import merchstoreList, merchstoreSublist, merchstoreItem

urlpatterns = [
    path('merchstore/items/', merchstoreList, name="merchstoreList"),
    path('merchstore/items/<str:product_type>', merchstoreSublist, name="merchstoreSublist"),
    path('merchstore/item/<int:num>/', merchstoreItem, name="merchstoreItem"),
    ]

#app_name = "merchstore"
