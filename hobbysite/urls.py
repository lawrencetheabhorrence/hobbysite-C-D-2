from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("admin/", admin.site.urls),
    path("wiki/", include("wiki.urls")),
    path("forum/", include("forum.urls")),
    path("blog/", include("blog.urls")),
    path("merchstore/", include("merchstore.urls")),
    path("commissions/", include("commissions.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("user/", include("user_management.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
