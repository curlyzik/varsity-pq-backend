import os
import environ
from datetime import timedelta
from pathlib import Path
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(("SECRET_KEY"))

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Local apps
    "users.apps.UsersConfig",
    "past_questions.apps.PastQuestionsConfig",
    # Third party apps
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "dj_rest_auth",
    "corsheaders",
    "cloudinary_storage",
    "cloudinary",
    "django_cleanup.apps.CleanupConfig",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "uni_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        # "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "uni_project.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# Static file configuration

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

MEDIA_URL = "media/"
# MEDIA_ROOT = BASE_DIR / "media"

# CLOUDINARY SETUP FOR FILE STORAGE
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.RawMediaCloudinaryStorage"
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": env(("CLOUDINARY_CLOUD_NAME")),
    "API_KEY": env(("CLOUDINARY_API_KEY")),
    "API_SECRET": env(("CLOUDINARY_API_SECRET")),
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CUSTOM USER MODEL
AUTH_USER_MODEL = "users.CustomUser"
SITE_ID = 1

# DJ-REST-AUTH SETTINGS
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    )
}

REST_USE_JWT = True
JWT_AUTH_COOKIE = "my-app-auth"
JWT_AUTH_REFRESH_COOKIE = "my-refresh-token"

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "users.serializers.CustomUserDetailsSerializer",
    "PASSWORD_RESET_CONFIRM_SERIALIZER": "users.serializers.CustomPasswordResetConfirmSerializer",
}

OLD_PASSWORD_FIELD_ENABLED = True

# SIMPLE_JWT SETTINGS
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
}

# CORSHEADERS SETTINGS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.3000",
    "http://192.168.22.42:3000",
    "https://varsity-pq.herokuapp.com",
    "https://varsity-pq-frontend.vercel.app",
    "https://varsitypq.com",
    "https://www.varsitypq.com",
]

# DJOSER SETTINGS
DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "password-reset-confirm/{uid}/{token}",
    "SERIALIZERS": {},
    "PERMISSIONS": {
        "password_reset": ["rest_framework.permissions.AllowAny"],
    },
}

# DEFAULT SITE NAME
SITE_NAME = "Varsity PQ"
