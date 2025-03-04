from django.shortcuts import render
from .models import Post


def index_view(request):
    return render(request, "forum/index.html", {"post_list": Post.objects.all()})


def detail_view(request, pk):
    return render(request, "forum/post_detail.html", {"post": Post.objects.get(id=pk)})
