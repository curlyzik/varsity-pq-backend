from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("past_questions.urls")),
        path("users/", include("users.urls")),
        path("dj-rest-auth/", include("dj_rest_auth.urls")),
        path("auth/", include("djoser.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
