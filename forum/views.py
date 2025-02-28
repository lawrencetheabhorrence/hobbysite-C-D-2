from django.views import generic

# Create your views here.
from .models import Post


class IndexView(generic.ListView):
    template_name = "forum/index.html"
    context_object_name = "post_list"

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "forum/post_detail.html"
