from .. import dto
from ..exceptions import InvalidEmail
from ..interfaces.mail import MailGateway
from ..utils import _validate_email


class SendMailService:
    def __init__(self, mail_gateway: MailGateway) -> None:
        self._mail = mail_gateway

    async def __call__(self, mail_data: dto.Mail) -> dto.MailStatus:
        if _validate_email(mail_data.to):
            return await self._mail.send_mail(mail_data=mail_data)

        raise InvalidEmail(email=mail_data.to)
