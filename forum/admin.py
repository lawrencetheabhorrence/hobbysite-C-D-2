from django.contrib import admin

from .models import PostCategory, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)
