from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from .models import ProductType, Product

def merchstoreList(request):
    return render(request, "merchstoreList.html", {"inventory": ProductType.objects.all()})

def merchstoreSublist(request, product_type=""):

    try:
        chosen_product_type = get_object_or_404(ProductType, name=product_type)
        available_items = get_list_or_404(Product, product_type=chosen_product_type)
        context = {"product_kind": chosen_product_type,
                   "items": available_items}
    except:
        return HttpResponseNotFound(loader.get_template("404.html").render())

    return render(request, "merchstoreSublist.html", context)

def merchstoreItem(request, num=0):

    item_range = range(1,len(Product.objects.all())+1)

    if num in item_range:

        product = Product.objects.get(productID=num)
        return render(request, "merchstoreItem.html", {"product": product})
    
    return HttpResponseNotFound(loader.get_template("404.html").render())
