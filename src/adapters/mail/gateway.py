from email.message import EmailMessage

import structlog
from aiosmtplib import SMTP

from src.business_logic.mail import dto
from src.business_logic.mail.enum import Status
from src.business_logic.mail.interfaces.mail import MailGateway

logger = structlog.stdlib.get_logger("structlog")


class MailGatewayImpl(MailGateway):
    def __init__(self, smtp_client: SMTP) -> None:
        self._client = smtp_client

    async def send_mail(self, mail_data: dto.Mail) -> dto.MailStatus:
        try:
            await self._client.send_message(
                message=self._make_message(
                    to=mail_data.to,
                    subject=mail_data.subject,
                    content=mail_data.message,
                )
            )
            logger.debug("Message sent success", extra={"to": mail_data.to})
            return dto.MailStatus(status=Status.SUCCESS)
        except Exception:
            logger.debug(
                "Message sent denied",
                extra={
                    "to": mail_data.to,
                    "request_id": structlog.contextvars.get_contextvars().get(
                        "request_id"
                    ),
                },
            )
            return dto.MailStatus(status=Status.DENIED)

    def _make_message(self, to: str, subject: str, content: str) -> EmailMessage:
        new_email = EmailMessage()
        new_email["From"] = self.from_email
        new_email["To"] = to
        new_email["Subject"] = subject
        new_email.set_content(content)

        return new_email

    @property
    def from_email(self) -> str:
        return self._client._login_username
