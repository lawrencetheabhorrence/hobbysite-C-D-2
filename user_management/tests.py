from django.test import TestCase, Client
from .models import Profile
from django.contrib.auth.models import User
from django.urls import reverse


class ProfileCreateCase(TestCase):
    def test_create_user(self):
        client = Client()
        client.post(
            reverse("user_management:register"),
            {
                "username": "testuser",
                "password": "password",
                "name": "Test User",
                "email_address": "test@testing.com",
            },
        )
        self.assertIsNotNone(Profile.objects.get(name="Test User"))
