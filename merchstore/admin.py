from django.contrib import admin
from .models import ProductType, Product


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType

    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ["name", "product_type", "price"]
    list_filter = ["product_type", "price", "name"]
    search_fields = ["product_type__name", "name"]


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
