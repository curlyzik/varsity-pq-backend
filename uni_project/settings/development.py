from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "192.168.104.42", "localhost"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DOMAIN = settings.ALLOWED_HOSTS[1] + ":3000"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
