from django.views.generic import ListView, DetailView
from .models import ThreadCategory, Thread


class ThreadListView(ListView):
    model = ThreadCategory
    template_name = "forum/index.html"
    context_object_name = "categories"

class ThreadDetailView(DetailView):
    model = Thread
    template_name = "forum/detail.html"
    context_object_name = "thread"
