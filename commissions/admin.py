from django.contrib import admin
from .models import Commission, Comment


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ("title", "description", "people_required", "created_on", "updated_on")
    list_filter = ("created_on", "people_required")
    list_display_links = ("title",)
    list_editable = ("description", "people_required")
    search_fields = ("title",)


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ("commission", "entry", "created_on", "updated_on")
    list_filter = ("created_on", "commission")
    search_fields = ("commission__title", "entry")
    list_display_links = ("commission",)
    list_editable = ("entry",)


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)