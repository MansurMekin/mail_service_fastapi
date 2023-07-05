from dataclasses import dataclass


@dataclass
class MailConfig:
    host: str
    username: str
    password: str
    port: int = 587
