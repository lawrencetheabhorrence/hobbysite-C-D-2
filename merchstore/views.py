from django.shortcuts import render
from django.http import HttpResponse

def merchstoreList(request):
    return HttpResponse("Here lies the list")

def merchstoreItem(request, num=0):
    return HttpResponse("Here lies item "+str(num))
