import logging
import sys

import structlog

from src.adapters.logger.config import LoggerConfig


def setup_logging(config: LoggerConfig) -> None:
    """Configure main logging"""
    _configure_structlog(config.json_format)
    _configure_default_logging(level=config.level, json_format=config.json_format)


def _build_default_processors(json_format):
    pr = [
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.contextvars.merge_contextvars,
        structlog.processors.CallsiteParameterAdder(
            parameters={
                structlog.processors.CallsiteParameter.PATHNAME,
                structlog.processors.CallsiteParameter.FILENAME,
                structlog.processors.CallsiteParameter.MODULE,
                structlog.processors.CallsiteParameter.FUNC_NAME,
                structlog.processors.CallsiteParameter.THREAD,
                structlog.processors.CallsiteParameter.THREAD_NAME,
                structlog.processors.CallsiteParameter.PROCESS,
                structlog.processors.CallsiteParameter.PROCESS_NAME,
            }
        ),
    ]
    if json_format:
        pr.append(structlog.processors.format_exc_info)

    return pr


def _configure_structlog(json_format) -> None:
    structlog.configure_once(
        processors=_build_default_processors(json_format=json_format)
        + [
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
    )


def _configure_default_logging(*, level, json_format: bool) -> None:
    renderer_processor = (
        structlog.processors.JSONRenderer()
        if json_format
        else structlog.dev.ConsoleRenderer()
    )

    formatter = structlog.stdlib.ProcessorFormatter(
        processors=_build_default_processors(json_format=json_format)
        + [
            structlog.stdlib.ProcessorFormatter.remove_processors_meta,
            renderer_processor,
        ],
    )

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(level)
