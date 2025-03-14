from django.db import models
from django.urls import reverse


class ProductType(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default="Some variety of items sold in this merch store.")

    class Meta:
        ordering = ["name"]
        verbose_name = "ProductType"
        verbose_name_plural = "ProductTypes"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("merchstore_variety", kwargs={"product_type":self.name})


class Product(models.Model):

    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, null=True, on_delete = models.SET_NULL, related_name = 'ProductType')
    price = models.DecimalField(max_digits=7,decimal_places=2)
    description = models.TextField(default="A buyable item of this merch store.")

    class Meta:
        ordering = ["name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("merchstore_item", kwargs={"num":self.id})
