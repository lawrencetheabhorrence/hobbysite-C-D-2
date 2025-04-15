from django.db import models
from django.urls import reverse
from user_management.models import Profile


class ProductType(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ["name"]
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"

    def __str__(self):
        return self.name


class Product(models.Model):


    class ProductStatusChoices(models.TextChoices):
            AVAILABLE = "Available"
            ON_SALE = "On Sale"
            OUT_OF_STOCK = "Out of Stock"


    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType, null=True, on_delete=models.SET_NULL, related_name="ProductType"
    )
    owner = models.ForeignKey(
        Profile, null=False, on_delete=models.CASCADE, related_name="Owner", default=""
    )
    description = models.TextField(default="A buyable item of this merch store.")
    price = models.DecimalField(max_digits=24, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=12,
        choices=ProductStatusChoices,
        default=ProductStatusChoices.OUT_OF_STOCK,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("merchstore_item", kwargs={"itemID": self.id})


class Transaction(models.Model):


    class TransactionStatusChoices(models.TextChoices):
        ON_CART = "On Cart"
        TO_PAY = "To Pay"
        TO_SHIP = "To Ship"
        TO_RECEIVE = "To Receive"
        DELIVERED = "Delivered"


    buyer = models.ForeignKey(
        Profile, null=True, on_delete=models.SET_NULL, related_name="Buyer"
    )
    product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL, related_name="Product"
    )
    amount = models.PositiveIntegerField()
    status = models.CharField(
        max_length=12,
        choices=TransactionStatusChoices,
        default=TransactionStatusChoices.ON_CART,
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["buyer"]
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return (
            self.buyer.name
            + "'s "
            + str(self.amount)
            + " "
            + self.product.name
            + " currently "
            + self.status
        )
