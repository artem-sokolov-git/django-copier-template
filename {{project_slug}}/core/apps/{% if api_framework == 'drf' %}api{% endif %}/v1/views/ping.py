from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.ping import PingSerializer


class PingAPIView(APIView):
    @extend_schema(
        summary="Ping endpoint",
        description="Simple ping endpoint that returns pong with timestamp",
        responses={200: PingSerializer},
        tags=["Health Check"],
    )
    def get(self, request: Request) -> Response:
        data = {
            "message": "pong",
            "timestamp": timezone.now(),
            "status": "ok",
        }
        serializer = PingSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
