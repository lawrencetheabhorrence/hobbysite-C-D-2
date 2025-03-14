from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from .models import ProductType, Product

def merchstoreList(request):
    return render(request, "merchstore/merchstore_list.html", {"inventory": ProductType.objects.all()})

def merchstoreVariety(request, product_type=""):

    chosen_product_type = get_object_or_404(ProductType, name=product_type)
    available_items = get_list_or_404(Product, product_type=chosen_product_type)

    context = {"product_kind": chosen_product_type,
                   "items": available_items}

    return render(request, "merchstore/merchstore_variety.html", context)

def merchstoreItem(request, itemID):
    product = get_object_or_404(Product, pk=itemID)

    return render(request, "merchstore/merchstore_item.html", {"product": product})
