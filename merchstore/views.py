from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ProductType, Product

def merchstoreList(request):

    context = {"inventory": []}

    for product_type in ProductType.objects.all():

        product_kind={"product_kind": product_type}
        items=[]
        products_under_kind = Product.objects.filter(product_type__name=product_type.__str__())

        for product in products_under_kind:
            items.append(product)

        product_kind["items"]=items
        context["inventory"].append(product_kind)

    return render(request, "merchstoreList.html", context)

def merchstoreSublist(request, product_type=""):

    available_types = {}

    for product_type_item in ProductType.objects.all():
        available_types[product_type_item.__str__()]=product_type_item

    if product_type in available_types:

        context={"product_kind": ProductType.objects.get(name=product_type)}
        items=[]
        products_under_type = Product.objects.filter(product_type__name=product_type.__str__())

        for product in products_under_type:
            items.append(product)

        context["items"]=items
        return render(request, "merchstoreSublist.html", context)

    return HttpResponse(loader.get_template("404.html").render())

def merchstoreItem(request, num=0):

    item_range = range(1,len(Product.objects.all())+1)

    if num in item_range:

        product = Product.objects.get(productID=num)
        return render(request, "merchstoreItem.html", {"product": product})
    
    return HttpResponse(loader.get_template("404.html").render())
