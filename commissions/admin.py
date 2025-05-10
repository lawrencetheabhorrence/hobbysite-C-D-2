from django.contrib import admin
from .models import Commission


class CommissionAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "status",
        "created_on",
        "updated_on",
    ]
    list_filter = ["created_on", "status"]
    search_fields = ["title"]
    list_display_links = ["title"]


admin.site.register(Commission, CommissionAdmin)
