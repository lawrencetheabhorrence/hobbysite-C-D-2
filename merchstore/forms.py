from django import forms
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from .models import Transaction, Product


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
