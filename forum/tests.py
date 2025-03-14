from django.test import TestCase

from .models import Post, PostCategory


# Create your tests here.
class PostCategoryModelTests(TestCase):
    def categories_by_name_ascending(self):
        """
        categories_by_name_ascending() returns True when
        post categories are arranged in ascending order
        by name.
        """
        PostCategory(name="abcd", description="wxyz").save()
        PostCategory(name="wxyz", description="abcd").save()
        return Post.objects.first.name < Post.objects.last


class PostModelTests(TestCase):
    def posts_by_create_date_descending(self):
        """
        posts_by_date_descending() returns True when
        posts are arranged in descending order by
        creation date.
        """
        test_category = PostCategory(name="test", description="test")
        test_category.save()
        Post(title="test_post 1", category=test_category, entry="lorem ipsum")
        Post(title="test_post 2", category=test_category, entry="lorem ipsum")

        return (
            Post.objects.first.name == "test_post 1"
            and Post.objects.last.name == "test_post 2"
        )
