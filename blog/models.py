from django.db import models

class ArticleCategory(models.Model):
    
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        
        return f"{self.name}"

    class Meta():

        ordering = ["name"]

class Article(models.Model):

    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, null=True, on_delete=models.SET_NULL)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return f"{self.title}, {self.category}, {self.entry}, {self.created_on}, {self.updated_on}"

    class Meta():

        ordering = ["-created_on"]

