from django.contrib import admin
from .models import ThreadCategory, Thread, Comment


class ThreadAdmin(admin.ModelAdmin):
    fields = ["title", "author", "category", "entry"]
    list_display = ["title", "author", "category", "created_on"]
    list_filter = ["category", "created_on"]
    search_fields = ["title", "entry"]
    readonly_fields = ["created_on", "updated_on"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["thread", "author", "created_on"]
    list_filter = ["created_on"]
    search_fields = ["entry"]
    readonly_fields = ["created_on", "updated_on"]


@admin.register(ThreadCategory)
class ThreadCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)
