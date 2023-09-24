from .common import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

SECRET_KEY = "django-insecure-jjnrx5$9420w(bkcou1s!h2ko@a+(1c(^l9kg9=a$57m7re7zp"

DEBUG = True

ALLOWED_HOSTS = ["*"]
