from django.db import models
from django.urls import reverse

class ProductType(models.Model):
    productTypeID = models.IntegerField(primary_key=True,default=0,editable=True)
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("merchstore:merchstoreSublist",kwargs={"product_type":str(self.name)})
    
    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        ordering = ['name']
        unique_together = ['name']
        verbose_name = 'ProductType'
        verbose_name_plural = 'ProductTypes'

    description = models.TextField(default="Some variety of items sold in this merch store.")

class Product(models.Model):
    productID = models.IntegerField(primary_key=True,default=0,editable=True)
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, null=True, on_delete = models.SET_NULL, related_name = 'ProductType')
    price = models.DecimalField(max_digits=7,decimal_places=2)
    
    def get_absolute_url(self):
        return reverse("merchstore:merchstoreItem",kwargs={"num":int(self.productID)})

    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        ordering = ['name']
        unique_together = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    description = models.TextField(default="A buyable item of this merch store.")
    
