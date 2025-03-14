from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from .models import ProductType, Product

def merchstoreList(request):
    return render(request, "merchstore/merchstoreList.html", {"inventory": ProductType.objects.all()})

def merchstoreSublist(request, product_type=""):

    try:
        chosen_product_type = get_object_or_404(ProductType, name=product_type)
        available_items = get_list_or_404(Product, product_type=chosen_product_type)
        context = {"product_kind": chosen_product_type,
                   "items": available_items}
    except:
        return HttpResponseNotFound(loader.get_template("merchstore/404.html").render())

    return render(request, "merchstore/merchstoreSublist.html", context)

def merchstoreItem(request, num=0):
    try:
        product = get_object_or_404(Product, pk=num)

    except:
        return HttpResponseNotFound(loader.get_template("merchstore/404.html").render())

    return render(request, "merchstore/merchstoreItem.html", {"product": product})
