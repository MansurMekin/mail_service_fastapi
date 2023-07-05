from pydantic import BaseSettings


class ConfigExtractor(BaseSettings):
    mail_host: str
    mail_username: str
    mail_password: str
    mail_port: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
