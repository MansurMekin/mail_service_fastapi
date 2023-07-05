from dataclasses import dataclass

from src.business_logic.common.dto.base import DTO

from ..enum import Status


@dataclass
class Mail(DTO):
    to: str
    subject: str
    message: str


@dataclass
class MailStatus(DTO):
    status: Status
