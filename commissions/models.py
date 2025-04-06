from django.db import models


class Commission(models.Model):
    class CommissionStatusOptions(models.TextChoices):
        OPEN = "Open"
        FULL = "Full"
        COMPLETED = "Completed"
        DISCONTINUED = "Discontinued"

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        default=CommissionStatusOptions.OPEN, choices=CommissionStatusOptions
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]


class Job(models.Model):
    class JobStatusOptions(models.TextChoices):
        OPEN = "Open"
        FULL = "Full"

    commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    role = models.TextField(max_length=255)
    manpower_required = models.PositiveIntegerField()
    status = models.CharField(default=JobStatusOptions.OPEN, choices=JobStatusOptions)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-status", "role"]
