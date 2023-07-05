import uuid
from collections.abc import Callable
from contextvars import ContextVar
from typing import Any

import structlog
from fastapi.requests import Request
from fastapi.responses import Response

request_id = ContextVar("request_id")

structlog_logger = structlog.stdlib.get_logger("structlog")


class LoggerMiddleware:
    async def __call__(self, request: Request, call_next: Callable[..., Any]) -> Any:
        value = request.headers.get("request-id", str(uuid.uuid4()))

        request_id.set(value)

        structlog_logger.debug("extract request id header", request_id=value)
        structlog.contextvars.clear_contextvars()
        structlog.contextvars.bind_contextvars(
            request_id=value,
        )

        response: Response = await call_next(request)

        return response
