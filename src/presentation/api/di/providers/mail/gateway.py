from aiosmtplib import SMTP
from fastapi import Depends

from src.adapters.mail.gateway import MailGatewayImpl
from src.business_logic.mail.interfaces.mail import MailGateway
from src.presentation.api.di.stub import Stub


def mail_gateway_provider(smtp_client: SMTP = Depends(Stub(SMTP))) -> MailGateway:
    return MailGatewayImpl(smtp_client=smtp_client)
