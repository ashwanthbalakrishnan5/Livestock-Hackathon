from .common import *
import dj_database_url


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "nevcykgoxnxvgyfr",
        "USER": "ocrrvxkapzuhefbh",
        "PASSWORD": "phksuujdhodxomva",
        "HOST": "13.233.194.98",
        "PORT": "8001",
    }
}

SECRET_KEY = "django-insecure-jjnrx5$9420w(bkcou1s!h2ko@a+(1c(^l9kg9=a$57m7re7zp"

DEBUG = True

ALLOWED_HOSTS = ["*"]
