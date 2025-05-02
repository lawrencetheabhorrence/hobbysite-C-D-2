from django.db import models
from user_management.models import Profile


class ArticleCategory(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):

        return f"{self.name}"

    class Meta:

        ordering = ["name"]


class Article(models.Model):

    title = models.CharField(max_length=255)
    author = models.OneToOneField(Profile, on_delete=models.SET_NULL)
    category = models.ForeignKey(ArticleCategory, null=True, on_delete=models.SET_NULL)
    entry = models.TextField()
    header_image = models.ImageField(null=True, upload_to="uploads/blog/%Y/%m/%d/")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.title}, {self.category}, {self.entry}, {self.created_on}, {self.updated_on}"

    class Meta:

        ordering = ["-created_on"]


class Comment(models.Model):

    author = models.ForeignKey(Profile, on_delete=models.SET_NULL)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.name}, {self.created_on}, {self.article.title}"

    class Meta:

        ordering = ["created_on"]
