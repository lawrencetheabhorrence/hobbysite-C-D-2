from django.test import TestCase
from .models import Article, ArticleCategory

<<<<<<< HEAD
from .models import Article, ArticleCategory

=======
>>>>>>> 587c4d94a55b9b5ac3273af78ed70296eeece7e7
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
<<<<<<< HEAD
        self.assertEqual(self.article.category.name, "Tech")
=======
        self.assertEqual(self.article.category.name, "Tech")
>>>>>>> 587c4d94a55b9b5ac3273af78ed70296eeece7e7
