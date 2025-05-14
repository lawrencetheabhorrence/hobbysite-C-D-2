from django.contrib import admin
from .models import Article, ArticleCategory, Comment


class ArticleAdmin(admin.ModelAdmin):
    fields = ["title", "category", "entry"]
    list_display = ["title", "category"]
    list_filter = ["category"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)
admin.site.register(Comment)
