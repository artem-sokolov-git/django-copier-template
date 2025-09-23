from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.ping import PingViewSet

router = DefaultRouter()
router.register(r"ping", PingViewSet, basename="ping")

urlpatterns = [
    path("", include(router.urls)),
]
