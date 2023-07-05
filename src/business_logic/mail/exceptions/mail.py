from dataclasses import dataclass

from src.business_logic.common.exceptions.base import AppException


@dataclass
class InvalidEmail(AppException):
    email: str

    @property
    def message(self) -> str:
        return "Invalid email"
