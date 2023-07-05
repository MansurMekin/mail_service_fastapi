from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from src.presentation.api.middlewares.logger import LoggerMiddleware


def setup_middlewares(app: FastAPI) -> None:
    logger_middleware = LoggerMiddleware()

    app.add_middleware(middleware_class=BaseHTTPMiddleware, dispatch=logger_middleware)
