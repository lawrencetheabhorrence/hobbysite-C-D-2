from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Article

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = [ 'title', 'author', 'category', 'entry', 'header_image' ]
    template_name = 'wiki/article_create.html'
