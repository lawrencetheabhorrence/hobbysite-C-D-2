from django.contrib import admin
from .models import ProductType, Product, Transaction


class ProductTypeAdmin(admin.ModelAdmin):

    model = ProductType

    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


class ProductAdmin(admin.ModelAdmin):

    model = Product

    list_display = ["name", "product_type", "price", "status"] #+"owner"
    list_filter = ["product_type", "name", "status"] #+"owner"
    search_fields = ["product_type__name", "name"]


class TransactionAdmin(admin.ModelAdmin):

    model = Transaction

    list_display = ["product", "amount", "status"] #+"buyer"
    list_filter = ["product"] #+"buyer"
    search_fields = ["product"] #+"buyer"

admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
