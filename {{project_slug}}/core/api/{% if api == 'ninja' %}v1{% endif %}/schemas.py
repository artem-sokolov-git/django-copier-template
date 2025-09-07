from datetime import datetime

from ninja import Schema


class PingResponseSchema(Schema):
    message: str
    timestamp: datetime
    status: str
