from django.contrib import admin
from .models import ProductType, Product


class ProductTypeAdmin(admin.ModelAdmin):

    model = ProductType

    list_display = (
        "name",
        "productTypeID",
    )
    list_filter = ("name",)
    list_display_links = ("productTypeID",)
    list_editable = ("name",)


class ProductAdmin(admin.ModelAdmin):

    model = Product

    list_display = (
        "name",
        "product_type",
        "price",
        "productID",
    )
    list_filter = ("product_type",)
    search_fields = ["product_type__name"]
    list_display_links = ("productID",)
    list_editable = (
        "name",
        "product_type",
        "price",
    )


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
