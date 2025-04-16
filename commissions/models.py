from django.db import models
from user_management.models import Profile


class Commission(models.Model):
    class CommissionStatusOptions(models.TextChoices):
        OPEN = "Open"
        FULL = "Full"
        COMPLETED = "Completed"
        DISCONTINUED = "Discontinued"

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=15,
        default=CommissionStatusOptions.OPEN,
        choices=CommissionStatusOptions,
    )
    # The list view requires us to track commissions created by the User but they don't have a creator field
    creator = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="commissions"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.title


class Job(models.Model):
    class JobStatusOptions(models.TextChoices):
        OPEN = "Open"
        FULL = "Full"

    commission = models.ForeignKey(
        Commission, on_delete=models.CASCADE, related_name="jobs"
    )
    role = models.TextField(max_length=255)
    manpower_required = models.PositiveIntegerField()
    status = models.CharField(
        max_length=15, default=JobStatusOptions.OPEN, choices=JobStatusOptions
    )

    class Meta:
        ordering = ["status", "-manpower_required", "role"]


class JobApplication(models.Model):
    class ApplicationStatusOptions(models.TextChoices):
        PENDING = "Pending"
        ACCEPTED = "Accepted"
        REJECTED = "Rejected"

    status = models.CharField(
        max_length=15,
        default=ApplicationStatusOptions.PENDING,
        choices=ApplicationStatusOptions,
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="applications"
    )
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["status", "-applied_on"]
