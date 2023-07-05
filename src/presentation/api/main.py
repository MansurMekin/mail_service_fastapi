from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from ...adapters.logger.main import setup_logging
from .controllers.main import setup_controllers
from .di.main import setup_di
from .lifespan import lifespan
from .middlewares.main import setup_middlewares
from .settings.config import Config


def build_app(config: Config) -> FastAPI:
    app = FastAPI(
        title="Mailer", default_response_class=ORJSONResponse, lifespan=lifespan
    )

    # Configuration Block
    setup_logging(config=config.logger)
    setup_middlewares(app=app)
    setup_controllers(app=app)
    setup_di(app=app, config=config)

    return app
