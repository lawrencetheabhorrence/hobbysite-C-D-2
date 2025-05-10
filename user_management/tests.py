from django.test import TestCase, Client
from .models import Profile, ProfileCreationForm
from .views import ProfileCreateView
from django.contrib.auth.models import User
from django.urls import reverse


# https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django
class ProfileCreateCase(TestCase):
    def test_create_user(self):
        form_data = {
            "username": "testuser",
            "password1": "oeainsoteanrostenoae1231341324",
            "password2": "oeainsoteanrostenoae1231341324",
            "name": "Test User",
            "email_address": "test@testing.com",
        }

        form = ProfileCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        profile = user.profile
        self.assertIsNotNone(Profile.objects.get(user=user))
        self.assertIsNotNone(profile)
        self.assertEqual(user.username, form_data["username"])
        self.assertEqual(profile.name, form_data["name"])
        self.assertEqual(profile.email_address, form_data["email_address"])
