from .common import *
import os
import dj_database_url

DATABASES = {"default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))}

DEBUG = os.environ.get("DEBUG")

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["*"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
