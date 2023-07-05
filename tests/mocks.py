from email.message import EmailMessage

from aiosmtplib import SMTP
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.business_logic.mail import dto
from src.business_logic.mail.enum import Status
from src.business_logic.mail.interfaces.mail import MailGateway
from src.presentation.api.controllers.main import setup_controllers
from src.presentation.api.di.main import setup_di
from src.presentation.api.di.stub import Stub
from src.presentation.api.settings.config import load_config


def build_test_app() -> FastAPI:
    app = FastAPI(title="TestMailer", default_response_class=ORJSONResponse)

    setup_controllers(app=app)
    setup_di(app=app, config=load_config())

    smtp_mock = SMTPClientMock()

    app.dependency_overrides[Stub(SMTP)] = lambda: smtp_mock

    return app


class ConfigExtractorMock:
    """Mock Config Extractor without env"""

    mail_host: str = "localhost"
    mail_username: str = "username"
    mail_password: str = "password"
    mail_port: int = 587


class MailGatewayMock(MailGateway):
    async def send_mail(self, mail_data: dto.Mail) -> dto.MailStatus:
        if mail_data.message and mail_data.subject and mail_data.to:
            return dto.MailStatus(status=Status.SUCCESS)
        return dto.MailStatus(status=Status.DENIED)


class MockError(Exception):
    pass


class SMTPClientMock:
    _login_username: str = "mock_string"

    async def send_message(self, message: EmailMessage):
        if (
            message["From"]
            and message["To"]
            and message["Subject"]
            and message.get_content()
        ):
            return
        raise MockError
