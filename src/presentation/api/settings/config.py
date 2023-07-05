from dataclasses import dataclass

from src.adapters.logger.config import LoggerConfig
from src.adapters.mail.config import MailConfig

from .extractor import ConfigExtractor


@dataclass
class APIConfig:
    host: str = "0.0.0.0"
    port: int = 8000


@dataclass
class Config:
    api: APIConfig
    mail: MailConfig
    logger: LoggerConfig


def load_config() -> Config:
    extractor = ConfigExtractor()

    return Config(
        api=APIConfig(),
        mail=MailConfig(
            host=extractor.mail_host,
            username=extractor.mail_username,
            password=extractor.mail_password,
            port=extractor.mail_port,
        ),
        logger=LoggerConfig(),
    )
