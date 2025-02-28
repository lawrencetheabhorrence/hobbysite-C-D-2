from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Post, PostCategory


class IndexView(generic.ListView):
    template_name = "forum/index.html"
    context_object_name = "post_list"

    def get_queryset(self):
        return PostCategory.objects.all()


def PostByCategoryView(request, category):
    posts = Post.objects.filter(category__name=category)
    return render(request, "forum/post_list.html", {"post_list": posts})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "forum/post_detail.html"
