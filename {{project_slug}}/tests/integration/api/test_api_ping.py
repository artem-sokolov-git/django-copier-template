import pytest
import requests
from django.conf import settings

docker_django_port = settings.DOCKER_DJANGO_PORT


@pytest.mark.parametrize("url", [f"http://127.0.0.1:{docker_django_port}/api/v1/ping"])
def test_ping_endpoint_with_requests(url):
    response = requests.get(url, timeout=10)

    assert response.status_code == 200
    data = response.json()

    assert data["message"] == "pong"
    assert data["status"] == "ok"
    assert "timestamp" in data
