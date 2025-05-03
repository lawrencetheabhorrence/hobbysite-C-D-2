from django import forms
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from .models import Transaction, Product, Profile, ProductType


class TransactionForm(forms.ModelForm):
    product = None

    def __init__(
        self,
        *args,
        item=None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.product = item

    class Meta:
        model = Transaction
        fields = ["amount"]

    def clean_amount(self):
        amount = self.cleaned_data["amount"]

        if amount != None and self.product != None:
            if self.product.stock < amount:
                raise ValidationError("Buying too much")
            if amount <= 0:
                raise ValidationError("You are buying nothing")

        return amount

    def clean(self):
        cleaned_data = super().clean()

        if not None in cleaned_data:
            return cleaned_data
        else:
            raise ValidationError("Something is missing")


"""
					{% for error in form.non_field_errors %}
						{{ error|escape }}
					{% endfor %}
"""


class ProductCreator(forms.ModelForm):
    owner = forms.ModelChoiceField(
        queryset=Profile.objects.all(), widget=forms.HiddenInput()
    )

    class Meta:
        model = Product
        fields = "__all__"

    def clean_product_type(self):
        product_type = self.cleaned_data["product_type"]
        if ProductType.objects.get(pk=product_type.pk):
            return product_type
        else:
            raise ValidationError("Product Type does not exist")

    def clean_stock(self):
        stock = self.cleaned_data["stock"]
        try:
            stock_as_int = int(stock)
            if stock_as_int == float(stock) and stock_as_int >= 0:
                return stock_as_int
            else:
                raise ValidationError("Not a Non-negative Integer Value")
        except ValueError:
            raise ValidationError("Not even a number!")

    def clean_price(self):
        price = str(self.cleaned_data["price"])
        error_messages = [None, None]
        try:
            price_as_float = float(price)
            price_split = price.split(".")
            if price_as_float <= 0:
                error_messages[0] = "Not a Non-negative Number"
            if len(price_split) != 1 and len(price_split[1]) >= 3:
                error_messages[1] = "Too many decimal places in this economy!"
            if error_messages[0] or error_messages[1]:
                error_messages[0] = (
                    "" if error_messages[0] is None else error_messages[0]
                )
                error_messages[1] = (
                    "" if error_messages[1] is None else error_messages[1]
                )
                raise ValidationError(error_messages[0] + "..." + error_messages[1])
            else:
                return price_as_float
        except ValueError:
            raise ValidationError("That's the wrong number!")

    def clean_status(self):
        STATUS_CHOICES = {
            "Out Of Stock": "Out Of Stock",
            "On Sale": "On Sale",
            "Available": "Available",
        }
        status = self.cleaned_data["status"]
        if status in STATUS_CHOICES.keys():
            return status
        else:
            raise ValidationError("Where did this status even come from?")

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)

        if not None in cleaned_data:
            return cleaned_data
        else:
            raise ValidationError("There are some lines missing")
