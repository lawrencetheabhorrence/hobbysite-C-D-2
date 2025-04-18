from django.test import TestCase
from user_management.models import Profile
from django.contrib.auth.models import User
from .models import Commission, Job, JobApplication


class CommissionModelTest(TestCase):
    def setUp(self):
        u = User.objects.create_user("test", "test@email.com", "testpass")
        user = Profile.objects.create(user=u, name="Test User", email_address=u.email)

        commission = Commission.objects.create(
            title="Sample Commission",
            description="This is a test commission.",
            creator=user,
        )

        job = Job.objects.create(
            commission=commission, role="Test job", manpower_required=1
        )

        application = JobApplication.objects.create(job=job, applicant=user)

    def test_fill_job_has_open(self):
        commission = Commission.objects.get(title="Sample Commission")
        self.assertEqual(commission.status, Commission.CommissionStatusOptions.OPEN)
        commission.fill_job()
        self.assertEqual(commission.status, Commission.CommissionStatusOptions.OPEN)

    def test_reject_applicant(self):
        application = JobApplication.objects.first()

        application.reject_application()
        self.assertEqual(
            application.status, JobApplication.ApplicationStatusOptions.REJECTED
        )

    def test_accept_applicant(self):
        application = JobApplication.objects.first()

        application.accept_application()
        self.assertEqual(
            application.status, JobApplication.ApplicationStatusOptions.ACCEPTED
        )

        job = application.job
        commission = job.commission
        self.assertEqual(job.manpower_required, 0)
        self.assertEqual(job.status, Job.JobStatusOptions.FULL)
        self.assertEqual(commission.status, Commission.CommissionStatusOptions.FULL)

    def test_with_another_open_job(self):
        commission = Commission.objects.first()
        Job.objects.create(commission=commission, role="Extra Job", manpower_required=1)

        application = JobApplication.objects.first()

        application.accept_application()
        self.assertEqual(
            application.status, JobApplication.ApplicationStatusOptions.ACCEPTED
        )

        job = application.job
        commission = job.commission
        self.assertEqual(job.manpower_required, 0)
        self.assertEqual(job.status, Job.JobStatusOptions.FULL)
        self.assertEqual(commission.status, Commission.CommissionStatusOptions.OPEN)
