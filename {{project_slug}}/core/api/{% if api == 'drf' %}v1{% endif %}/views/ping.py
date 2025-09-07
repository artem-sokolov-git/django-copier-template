from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from ..serializers.ping import PingSerializer


class PingViewSet(viewsets.GenericViewSet):
    serializer_class = PingSerializer

    @extend_schema(
        summary="Ping endpoint",
        description="Simple ping endpoint that returns pong with timestamp",
        responses={200: PingSerializer},
        tags=["Health Check"],
    )
    def list(self, request: Request) -> Response:
        serializer = self.get_serializer(data={})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
