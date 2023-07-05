import contextlib

import structlog
from fastapi import FastAPI

from src.adapters.mail.main import create_smtp_client
from src.presentation.api.settings.config import load_config

logger = structlog.stdlib.get_logger("structlog")


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    logger.debug(event="Configure lifespan...")

    config = load_config()

    """"""
    smtp_client = create_smtp_client()
    await smtp_client.connect(
        hostname=config.mail.host,
        port=config.mail.port,
        username=config.mail.username,
        password=config.mail.password,
    )

    app.state.smtp_client = smtp_client

    yield

    app.state.smtp_client.close()
    del app.state.smtp_client
