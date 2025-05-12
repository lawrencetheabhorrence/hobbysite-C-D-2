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

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self.update_status(commit=False)

    class ProductStatusChoices(models.TextChoices):
        AVAILABLE = "Available"
        ON_SALE = "On Sale"
        OUT_OF_STOCK = "Out Of Stock"

    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType, null=True, on_delete=models.SET_NULL, related_name="products"
    )
    owner = models.ForeignKey(
        Profile,
        null=False,
        on_delete=models.CASCADE,
        related_name="products",
        default="",
    )
    description = models.TextField(default="A buyable item of this merch store.")
    price = models.DecimalField(max_digits=24, decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=12,
        choices=ProductStatusChoices,
        default=ProductStatusChoices.AVAILABLE,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("merchstore_item", kwargs={"itemID": self.id})

    def update_status(self, commit=True):
        if self.status == self.ProductStatusChoices.OUT_OF_STOCK and self.stock > 0:
            self.status = self.ProductStatusChoices.AVAILABLE
        elif self.status == self.ProductStatusChoices.AVAILABLE and self.stock == 0:
            self.status = self.ProductStatusChoices.OUT_OF_STOCK
        if commit:
            self.save()

    def reduce_stock(self, value):
        if value > self.stock:
            raise ValueError(
                f"You only have {self.stock} left in stock. You tried to reduce stock by {value} which is more than what is in stock."
            )
        self.stock = self.stock - value
        self.update_status()
        self.save()


class Transaction(models.Model):

    class TransactionStatusChoices(models.TextChoices):
        ON_CART = "On Cart"
        TO_PAY = "To Pay"
        TO_SHIP = "To Ship"
        TO_RECEIVE = "To Receive"
        DELIVERED = "Delivered"

    buyer = models.ForeignKey(
        Profile, null=True, on_delete=models.SET_NULL, related_name="transaction"
    )
    product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL, related_name="transaction"
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
            + " instances of "
            + self.product.name
        )
        # Ex: Dino's 5 instances of Chicken Nugget
