from django import template
from ..models import Product

register = template.Library()


@register.filter
def products(product_type):
    return Product.objects.filter(product_type=product_type)
