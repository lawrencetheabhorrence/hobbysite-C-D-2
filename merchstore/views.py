from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import ProductType, Product #, Transaction


def productList(request):
    return render(
        request,
        "merchstore/product_list.html",
        {"product_list": Product.objects.all()},
    )

'''
def merchstoreVariety(request, product_type=""):
    # This function is deprecated
    # Shows products of a certain type

    chosen_product_type = get_object_or_404(ProductType, name=product_type)
    available_items = get_list_or_404(Product, product_type=chosen_product_type)

    context = {"product_kind": chosen_product_type, "items": available_items}

    return render(request, "merchstore/merchstore_variety.html", context)
'''

def productDetail(request, itemID):
    product = get_object_or_404(Product, pk=itemID)

    return render(request, "merchstore/product_detail.html", {"product": product})

'''
def productCreate(request):

def productUpdate(request, itemID):

def cartContents(request):

def transactionList(request):

'''
