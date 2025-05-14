from django.contrib import admin
from .models import Commission, Job, JobApplication


class JobInline(admin.TabularInline):
    model = Job


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
    inlines = [JobInline]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(JobApplication)
