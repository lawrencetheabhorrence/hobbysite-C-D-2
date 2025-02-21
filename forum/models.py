from django.db import models


class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
