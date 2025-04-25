from django.db import models
from user_management.models import Profile


class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name="threads")
    category = models.ForeignKey(ThreadCategory, null=True, on_delete=models.SET_NULL, related_name="threads")
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]  

    def __str__(self):
        return f"Comment by {self.author.display_name} on {self.thread.title}"
