from django.test import TestCase
from .models import Commission, Comment


class CommissionModelTest(TestCase):
    def setUp(self):
        self.commission = Commission.objects.create(
            title="Sample Commission",
            description="This is a test commission.",
            people_required=3,
        )
        self.commission.save()

    def test_commission_creation(self):
        self.assertEqual(self.commission.title, "Sample Commission")
        self.assertEqual(self.commission.description, "This is a test commission.")
        self.assertEqual(self.commission.people_required, 3)


class CommentModelTest(TestCase):
    def setUp(self):
        self.commission = Commission.objects.create(
            title="Sample Commission",
            description="This is a test commission.",
            people_required=3,
        )
        self.commission.save()

        self.comment = Comment.objects.create(
            commission=self.commission, entry="This is a test comment."
        )
        self.comment.save()

    def test_comment_creation(self):
        self.assertEqual(self.comment.entry, "This is a test comment.")
        self.assertEqual(self.comment.commission.title, "Sample Commission")


# Create your tests here.
