from typing import Protocol

from src.business_logic.mail import dto


class MailGateway(Protocol):
    async def send_mail(self, mail_data: dto.Mail) -> dto.MailStatus:
        ...
