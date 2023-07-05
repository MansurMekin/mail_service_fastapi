from aiosmtplib import SMTP
from fastapi import Depends

from src.adapters.mail.config import MailConfig
from src.adapters.mail.main import create_smtp_client
from src.presentation.api.di.stub import Stub


async def provide_smtp_client(
    mail_config: MailConfig = Depends(Stub(MailConfig)),
) -> SMTP:
    async with create_smtp_client(config=mail_config) as client:
        yield client
