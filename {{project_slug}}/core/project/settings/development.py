from .base import *

DEBUG = True

if DATABASES["default"]["HOST"] != "localhost":
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
