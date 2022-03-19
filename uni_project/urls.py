from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

...

schema_view = get_schema_view(
    openapi.Info(
        title="Varsity PQ Api",
        default_version="v1",
        description="Varsity PQ API",
        #   terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@varsitypq.com"),
        #   license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("past_questions.urls")),
        path("users/", include("users.urls")),
        path("dj-rest-auth/", include("dj_rest_auth.urls")),
        path("auth/", include("djoser.urls.base")),
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
