from django.contrib import admin
from .models import ProductType, Product


class ProductTypeAdmin(admin.ModelAdmin):

    model = ProductType

    list_display = ("name","id",)
    list_filter = ("name",)
    search_fields = ["name"]
    list_display_links = ("id",)
    list_editable = ("name",)


class ProductAdmin(admin.ModelAdmin):

    model = Product

    list_display = ("name","product_type","price","id",)
    list_filter = ("product_type","price","name")
    search_fields = ["product_type__name","name"]
    list_display_links = ("id",)
    list_editable = ("name","product_type","price",)


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
