from rest_framework import serializers


class PingSerializer(serializers.Serializer):
    message = serializers.CharField(default="pong", read_only=True)
    timestamp = serializers.DateTimeField(read_only=True)
    status = serializers.CharField(default="ok", read_only=True)
