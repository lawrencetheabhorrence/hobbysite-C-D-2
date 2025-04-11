from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    '''
        Extension of user model\n
        has fields:\n
            name - max length of 63 characters
            email_address - email field
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=63)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return self.name
