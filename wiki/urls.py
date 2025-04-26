from django.urls import path
# from . import views
from .views import ArticleCreateView

app_name = "wiki"
urlpatterns = [
    path('article/add/', ArticleCreateView.as_view(), name='article-create')
]
