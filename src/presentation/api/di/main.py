from aiosmtplib import SMTP
from fastapi import FastAPI

from src.business_logic.mail.interfaces.mail import MailGateway
from src.business_logic.mail.services.send_mail import SendMailService

from ..settings.config import Config
from .providers.mail.gateway import mail_gateway_provider
from .providers.services.mail import get_send_mail_service
from .stub import Stub


def setup_di(app: FastAPI, config: Config) -> None:
    # Setup Mail Dependencies
    app.dependency_overrides[Stub(SMTP)] = lambda: app.state.smtp_client
    app.dependency_overrides[Stub(MailGateway)] = mail_gateway_provider
    app.dependency_overrides[Stub(SendMailService)] = get_send_mail_service
