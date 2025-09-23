from django.urls import path
from ninja import NinjaAPI

from .handlers import ping

api = NinjaAPI(version="1.0.0", title="V1 API")

api.get("/ping")(ping)

urlpatterns = [
    path("", api.urls),
]
