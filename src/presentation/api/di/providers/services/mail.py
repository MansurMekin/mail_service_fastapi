from fastapi import Depends

from src.business_logic.mail.interfaces.mail import MailGateway
from src.business_logic.mail.services.send_mail import SendMailService
from src.presentation.api.di.stub import Stub


def get_send_mail_service(
    smtp_gateway: MailGateway = Depends(Stub(MailGateway)),
) -> SendMailService:
    return SendMailService(mail_gateway=smtp_gateway)
