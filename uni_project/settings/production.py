from .base import *
import django_heroku

DEBUG = False

# Amazon S3 Configurations
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = env(('AWS_ACCESS_KEY_ID'))
AWS_SECRET_ACCESS_KEY = env(('AWS_SECRET_ACCESS_KEY'))
AWS_STORAGE_BUCKET_NAME = env(('AWS_STORAGE_BUCKET_NAME'))
AWS_QUERYSTRING_AUTH = False

# Static file configuration
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# heroku configuration
django_heroku.settings(locals())