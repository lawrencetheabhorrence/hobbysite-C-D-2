from django.contrib import admin
from .models import Commission, Job, JobApplication


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


class JobAdmin(admin.ModelAdmin):
    list_display = ["commission", "role", "status", "manpower_required"]
    list_filter = ["status"]
    search_fields = ["commission", "role"]
    list_display_links = ["role"]


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ["job", "status", "applicant"]
    list_filter = ["job", "status", "applicant"]
    search_fields = ["job", "applicant"]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
