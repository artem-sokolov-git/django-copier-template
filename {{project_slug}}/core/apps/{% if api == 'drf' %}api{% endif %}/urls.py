from django.urls import include, path

urlpatterns = [
    path("v1/", include("core.apps.api.v1.urls")),
]
