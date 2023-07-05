from aiosmtplib import SMTP

from src.adapters.mail.config import MailConfig


def create_smtp_client(config: MailConfig | None = None) -> SMTP:
    """Returns SMTP-Client"""

    return SMTP()
