from django.test import TestCase, Client
from .models import Article, ArticleCategory
from django.contrib.auth.models import User
from user_management.models import Profile


class ArticleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.profile = Profile.objects.create(user=self.user, name="name")
        self.cat_news = ArticleCategory.objects.create(name="News", description="")
        self.cat_tech = ArticleCategory.objects.create(name="Tech", description="")

    def test_article_written_by_profile(self):
        article = Article.objects.create(
            title="Title",
            author=self.profile,
            article_category=self.cat_news,
            entry="Entry",
        )

        self.assertEqual(article.title, "Title")
        self.assertEqual(article.author, "name")
        self.assertEqual(article.category, self.cat_news)
