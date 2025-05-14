from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
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

    def get_absolute_url(self):
        return reverse("commissions:commission_detail", kwargs={"pk": self.pk})

    def fill_job(self):
        """
        This method is called everytime a job is filled. It then checks if all jobs are filled and updates the status of the commission.
        """

        if self.status in [
            self.CommissionStatusOptions.COMPLETED,
            self.CommissionStatusOptions.DISCONTINUED,
        ]:
            return

        if not (self.jobs.filter(status=Job.JobStatusOptions.OPEN).exists()):
            self.status = self.CommissionStatusOptions.FULL
            self.save()


class Job(models.Model):
    class JobStatusOptions(models.TextChoices):
        OPEN = "Open"
        FULL = "Full"

    commission = models.ForeignKey(
        Commission, on_delete=models.CASCADE, related_name="jobs"
    )
    role = models.TextField(max_length=255)
    manpower_required = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(
        max_length=15, default=JobStatusOptions.OPEN, choices=JobStatusOptions
    )

    class Meta:
        ordering = ["status", "-manpower_required", "role"]

    def __str__(self):
        return self.role

    def get_absolute_url(self):
        return reverse("commissions:job_view", kwargs={"pk": self.pk})

    def open_manpower(self):
        accepted_applicants = JobApplication.objects.filter(
            job=self.id, status=JobApplication.ApplicationStatusOptions.ACCEPTED
        ).count()
        return self.manpower_required - accepted_applicants

    def accept_applicant(self):
        if self.open_manpower() == 0:
            self.set_full()

    def set_full(self):
        self.status = self.JobStatusOptions.FULL
        self.save()
        self.commission.fill_job()


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

    def get_absolute_url(self):
        return reverse("commissions:job_view", kwargs={"pk": self.job.pk})

    def __str__(self):
        return f"Application for {self.job}"

    def accept_application(self):
        self.status = self.ApplicationStatusOptions.ACCEPTED
        self.save()
        self.job.accept_applicant()

    def reject_application(self):
        self.status = self.ApplicationStatusOptions.REJECTED
        self.save()
