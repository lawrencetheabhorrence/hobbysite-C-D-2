from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Profile(models.Model):
    """
    Extension of user model
    has fields:
    name - max length of 63 characters
    email_address - email field
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=63)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return self.name


# https://forum.djangoproject.com/t/extending-the-existing-user-model/15773/2
class ProfileCreationForm(UserCreationForm):
    """
    Extends from the UserCreationForm to
    create a user from a username, password,
    name, and email.
    """

    name = forms.CharField(max_length=63)
    email_address = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "name",
            "email_address",
        )

    def save(self, *args, **kwargs):
        # First, save the user
        user = super().save(*args, **kwargs)
        # Then, create the profile
        Profile.objects.create(
            user=user,
            name=self.cleaned_data.get("name"),
            email_address=self.cleaned_data.get("email"),
        )
