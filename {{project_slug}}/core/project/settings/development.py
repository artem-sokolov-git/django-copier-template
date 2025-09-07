from . import env
from .base import *

DEBUG = True

if DATABASES["default"]["HOST"] != "localhost":
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

DOCKER_DJANGO_PORT = env.str("DOCKER_DJANGO_PORT", "8000")
