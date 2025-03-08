from django.test import TestCase

from .models import Article, ArticleCategory

class ArticleModelTest(TestCase):
    def setUp(self):
        self.category = ArticleCategory.objects.create(name="Tech", description="Tech articles")
        self.article = Article.objects.create(
            title="Sample Article",
            category=self.category,
            entry="This is a test entry."
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, "Sample Article")
        self.assertEqual(self.article.category.name, "Tech")