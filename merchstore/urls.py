from django.urls import path
from .views import merchstoreList, merchstoreItem

urlpatterns = [
    path('items/', merchstoreList, name="merchstoreList"),
    path('items/<str:product_type>', merchstoreSublist, name="merchstoreSublist"),
    path('item/<int:num>/', merchstoreItem, name="merchstoreItem"),
    ]

app_name = "merchstore"
