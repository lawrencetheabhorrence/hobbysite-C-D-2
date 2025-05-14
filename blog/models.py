from django.db import models
from django.urls import reverse
from user_management.models import Profile


class ArticleCategory(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:

        ordering = ["name"]

    def __str__(self):

        return f"{self.name}"


class Article(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, related_name="blog_articles"
    )
    category = models.ForeignKey(
        ArticleCategory, null=True, on_delete=models.SET_NULL, related_name="articles"
    )
    entry = models.TextField()
    header_image = models.ImageField(
        upload_to="blog/images/", default="images/placeholder.png"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_on"]

    def __str__(self):

        return f"{self.title}, {self.category}, {self.entry}, {self.created_on}, {self.updated_on}"

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"pk": self.id})


class Comment(models.Model):

    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, related_name="blog_comments", null=True
    )
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
