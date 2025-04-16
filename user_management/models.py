from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class ProfileCreationForm(UserCreationForm):
    """
    Extends from the UserCreationForm to
    create a user from a username, password,
    name, and email.
    """

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "name",
            "email_address",
        )
