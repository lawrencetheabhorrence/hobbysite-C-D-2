from django.contrib import admin
from .models import Commission, Comment


class CommissionAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "people_required",
        "created_on",
        "updated_on",
    ]
    list_filter = ["created_on", "people_required"]
    search_fields = ["title"]
    list_display_links = ["title"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["commission", "entry", "created_on", "updated_on"]
    list_filter = ["created_on", "commission"]
    search_fields = ["commission__title", "entry"]
    list_display_links = ["commission"]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)
