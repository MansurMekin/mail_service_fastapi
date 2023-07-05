from fastapi import FastAPI, Request, status
from fastapi.responses import ORJSONResponse

from src.business_logic.common.exceptions.base import AppException
from src.business_logic.mail.exceptions import InvalidEmail
from src.presentation.api.controllers.responses.exceptions import ErrorResult


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        exc_class_or_status_code=Exception, handler=unknown_exception_handler
    )
    app.add_exception_handler(
        exc_class_or_status_code=InvalidEmail,
        handler=email_validation_exception_handler,
    )


async def email_validation_exception_handler(
    request: Request, err: InvalidEmail
) -> ORJSONResponse:
    return await handle_error(
        request=request, err=err, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


async def unknown_exception_handler(request: Request, err: Exception) -> ORJSONResponse:
    return ORJSONResponse(
        content=ErrorResult(message="Unknown server error has occurred", data=err),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


async def handle_error(
    request: Request, err: AppException, status_code: int
) -> ORJSONResponse:
    return ORJSONResponse(
        content=ErrorResult(message=err.message, data=err),
        status_code=status_code,
    )
