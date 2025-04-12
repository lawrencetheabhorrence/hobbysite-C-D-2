from django.contrib import admin
from .models import ProductType, Product, Transaction


class ProductTypeAdmin(admin.ModelAdmin):

    model = ProductType

    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


class ProductAdmin(admin.ModelAdmin):

    model = Product

    list_display = ["name", "product_type", "price", "owner", "status"]
    list_filter = ["product_type", "name", "owner", "status"]
    search_fields = ["product_type__name", "name"]


class TransactionAdmin(admin.ModelAdmin):

    model = Transaction

    list_display = ["buyer", "product", "amount", "status"]
    list_filter = ["buyer", "product"]
    search_fields = ["buyer", "product"]


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
