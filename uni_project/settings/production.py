from .base import *
import django_heroku

ALLOWED_HOSTS = [
    "https://varsity-pq.herokuapp.com",
    "varsitypq.com",
    "www.varsitypq.com",
    "https://varsity-pq-frontend.vercel.app",
]

DOMAIN = settings.ALLOWED_HOSTS[1]

DEBUG = False


# Static file configuration
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# POST MARK EMAIL SERVICE PROVIDE FOR PASSWORD RESET
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env(("EMAIL_HOST"))
EMAIL_HOST_USER = env(("EMAIL_HOST_USER"))
EMAIL_HOST_PASSWORD = env(("EMAIL_HOST_PASSWORD"))
EMAIL_PORT = 2525
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = "<contact@varsitypq.com>"

# heroku configuration
django_heroku.settings(locals())