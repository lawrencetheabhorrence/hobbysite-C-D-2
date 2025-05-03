from django import template
from ..models import Product, Profile, Transaction

register = template.Library()

"""
@register.filter
def products(product_type):
    return Product.objects.filter(product_type=product_type)


@register.filter
def count_owner_products(owner):
    return len(Product.objects.filter(owner=owner))
"""


@register.filter
def person(pk):
    return Profile.objects.get(pk=pk)


@register.filter
def everyone_else(user):
    return Profile.objects.exclude(name=user)


@register.filter
def customer_of(user, otheruser):
    if Transaction.objects.filter(buyer=user, product__owner=otheruser):
        return True


@register.filter
def clerk_of(user, otheruser):
    if Transaction.objects.filter(buyer=otheruser, product__owner=user):
        return True
