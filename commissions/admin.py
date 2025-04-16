from django.contrib import admin
from .models import Commission


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


admin.site.register(Commission, CommissionAdmin)
