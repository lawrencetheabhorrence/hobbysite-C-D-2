from django.contrib import admin
from .models import ArticleCategory, Article


class ArticleAdmin(admin.ModelAdmin):
    fields = ["title", "category", "entry"]  # Specify fields manually
    list_display = [
        field.name for field in Article._meta.fields
    ]  # Keep dynamic field retrieval
    list_filter = ["category"]
    search_fields = ["title"]


# Register models
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)
