from django.http import HttpRequest
from django.utils import timezone

from .schemas import PingResponseSchema


def ping(request: HttpRequest) -> PingResponseSchema:
    return PingResponseSchema(message="pong", timestamp=timezone.now(), status="ok")
