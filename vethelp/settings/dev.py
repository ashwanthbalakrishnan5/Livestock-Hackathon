from .common import *
import dj_database_url


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "rdfxsempzpaxbxgk",
        "USER": "blxgmpfbdpirgcjx",
        "PASSWORD": "gpnfmjqjbbogxdzv",
        "HOST": "43.204.148.230",
        "PORT": "8001",
    }
}

SECRET_KEY = "django-insecure-jjnrx5$9420w(bkcou1s!h2ko@a+(1c(^l9kg9=a$57m7re7zp"

DEBUG = True

ALLOWED_HOSTS = ["*"]
