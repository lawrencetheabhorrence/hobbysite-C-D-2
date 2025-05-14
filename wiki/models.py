from django.db import models
from django.urls import reverse
from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile, null=True, on_delete=models.SET_NULL, related_name="wiki_articles"
    )
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name="articles",
    )
    header_image = models.ImageField(
        upload_to="wiki/images/", default="images/placeholder.png"
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse("wiki:article_detail", kwargs={"pk": self.id})


class Comment(models.Model):
    author = models.ForeignKey(
        Profile, null=True, on_delete=models.SET_NULL, related_name="wiki_comments"
    )
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment by {self.author} on {self.article.title}"


class Image(models.Model):
    article = models.ForeignKey(
        Article, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="wiki/images/")
    description = models.TextField()

    def __str__(self):
        return f"Image for {self.article.title}"
        return self.title
