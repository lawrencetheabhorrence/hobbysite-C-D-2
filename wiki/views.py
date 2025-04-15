# Article List View
# List ALL articles in the system, grouped by their category, and only show their title.
# The title is a link to the Wiki Detail View.
# When logged in, articles that are created by the logged-in user are in a separate group regardless of category. They should also be removed from the All Articles list.
# User's Articles should come before All Articles.
# In this view, there should be a link that will lead to the creation of an article.

# Article Detail View
# The view should show at least two more links of Articles that belong to the same category, ensuring that the displayed article does not appear in these links. (Think of this like a "Read More from <Category>")
# The view should show at least one image.
# This view should have a link to go back to the Article List View.
# Existing Comments should appear after the Comment Form, where comments are sorted by their Created On field where the most recent appears first
# This view should contain a Comment Form, which is only visible to logged-in users.
# This Comment form should be handled by the FBV/CBV that is handling the rendering of this page.
# In this view, if the Article's owner is the logged-in user, there should be an edit link that will lead to the update view.
# BONUS: Add an image gallery for the wiki page.

# Article Create View
# All fields should be available. The Created On and Updated On is automatically set, and the Author is the logged in user. These three fields should not be editable.
# Category field should be a dropdown.
# This should only be accessible to logged-in users.

# Article Update View
# It should allow updates of all fields except for the Created On and Author field.
# This should only be accessible to logged-in users.

# https://www.freecodecamp.org/news/how-to-use-defaultdict-python/


from django.shortcuts import render
from .models import Article
from collections import defaultdict 

def article_list(request):

    user_articles = []
    categorized_articles = defaultdict(list)
    articles = Article.objects.select_related("category", "author")

    if request.user.is_authenticated and hasattr(request.user, "profile"):
        user_profile = request.user.profile
        user_articles = articles.filter(author = user_profile)
        articles = articles.exclude(author = user_profile)

    for article in articles: 
        if article.category:
            categorized_articles[article.category.name].append(article)

    context = {
        "user_articles": user_articles,
        "categorized_articles": dict(categorized_articles),
    }

    return render(request, "wiki/article_list.html", context)
