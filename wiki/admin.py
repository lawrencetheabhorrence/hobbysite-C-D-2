from django.contrib import admin
from .models import ArticleCategory, Article

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  
    search_fields = ("name",)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.fields]  
    list_filter = ("category",)  
    search_fields = ("title",)  
