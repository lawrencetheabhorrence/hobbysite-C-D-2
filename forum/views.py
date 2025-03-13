from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post


def index_view(request):
    return render(request, "forum/index.html", {"post_list": get_list_or_404(Post)})


def detail_view(request, pk):
    return render(
        request, "forum/post_detail.html", {"post": get_object_or_404(Post, pk=pk)}
    )
