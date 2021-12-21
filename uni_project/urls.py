from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('past_questions.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]