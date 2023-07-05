from fastapi import FastAPI

from .exceptions import setup_exception_handlers
from .mail import router as post_router


def setup_controllers(app: FastAPI) -> None:
    app.include_router(router=post_router)

    setup_exception_handlers(app=app)
