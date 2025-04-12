from django.db import models
from django.urls import reverse
#from user_management.models import Profile


class ProductType(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()


    class Meta:
        ordering = ["name"]
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"


    def __str__(self):
        return self.name

    #May get deleted...unless there's still time
    '''
    def get_absolute_url(self):
        return reverse("merchstore_variety", kwargs={"product_type": self.name})
    '''


class Product(models.Model):
    STATUS_CHOICES = {
        "Available": "Available",
        "On Sale": "On Sale",
        "Out of Stock": "Out of Stock"
    }

    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType, null=True, on_delete=models.SET_NULL, related_name="ProductType"
        )
    '''
    owner = models.ForeignKey(
        Profile, null=False, on_delete=models.CASCADE, related_name="Owner"
        )
    '''
    description = models.TextField(default="A buyable item of this merch store.")
    price = models.DecimalField(max_digits=24, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="Out of Stock")


    class Meta:
        ordering = ["name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("merchstore_item", kwargs={"itemID": self.id})


class Transaction(models.Model):
    STATUS_CHOICES = {
        "On Cart": "On Cart",
        "To Pay": "To Pay",
        "To Ship": "To Ship",
        "To Receive": "To Receive",
        "Delivered": "Delivered",
    }
    '''
    buyer = models.ForeignKey(
        Profile, null=True, on_delete=models.SET_NULL, related_name="Buyer"
        )
    '''
    product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL, related_name="Product"
        )
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        #ordering = ["buyer"]
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return "Buyer's "+str(self.amount)+" "+self.product.name+" currently "+self.status
