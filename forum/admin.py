from django.contrib import admin

from .models import PostCategory, Post


class PostAdmin(admin.ModelAdmin):
    fields = ["title", "category", "entry"]
    list_display = ["title", "category"]
    list_filter = ["category"]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
