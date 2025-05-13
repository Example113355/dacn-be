# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

ALLOWED_HOSTS = ["digifarm.click", "127.0.0.1", "206.189.154.73"]

DEBUG = os.getenv("DEBUG", False)

STATIC_ROOT = os.path.join(BASE_DIR, "static")

# INSTALLED_APPS += ["storages"]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "prod_db"),
        "USER": os.getenv("DB_USER", "postgres"),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

# Sentry
# sentry_sdk.init(
#     dsn=os.getenv("SENTRY_DNS"),
#     enable_tracing=True,
#     integrations=[
#         DjangoIntegration(
#             transaction_style="url",
#             middleware_spans=True,
#             signals_spans=False,
#             cache_spans=False,
#         ),
#     ],
# )

# # boto3
# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#     },
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#     },
# }
# AWS_S3_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
# AWS_S3_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", "us-east-2")
# AWS_S3_SIGNATURE_VERSION = os.getenv("AWS_S3_SIGNATURE_VERSION", "s3v4")
# AWS_S3_FILE_OVERWRITE = str(os.getenv("AWS_S3_FILE_OVERWRITE", False)).lower() == "true"
# AWS_QUERYSTRING_AUTH = str(os.getenv("AWS_QUERYSTRING_AUTH", False)).lower() == "true"

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
    },
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        # "sentry": {
        #     "level": "ERROR",
        #     "filters": ["require_debug_false"],
        #     "class": "raven.contrib.django.handlers.SentryHandler",
        # },
    },
    "loggers": {
        "django": {
            # "handlers": ["console", "sentry"],
            "handlers": ["console"],
            "propagate": True,
            "level": "INFO",
        },
    },
}
