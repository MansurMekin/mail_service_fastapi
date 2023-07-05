import asyncio
from collections.abc import AsyncGenerator, Generator
from typing import Any

import pytest
import pytest_asyncio
from httpx import AsyncClient

from src.business_logic.mail.dto import Mail
from src.business_logic.mail.services.send_mail import SendMailService
from tests.mocks import MailGatewayMock, build_test_app


@pytest_asyncio.fixture(scope="function")
async def client() -> AsyncGenerator[AsyncClient, Any]:
    async with AsyncClient(app=build_test_app(), base_url="http://test") as test_client:
        yield test_client


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
def success_emails() -> list[str]:
    return [
        "email@mail.ru",
        "luckybatyr@yandex.ru",
        "pythontest@gmail.com",
    ]


@pytest.fixture(scope="function")
def invalid_emails() -> list[str]:
    return ["blablabla", "mockdata@@@@mail@.ru", "mockemail@mail.asd"]


@pytest.fixture(scope="function")
def mock_success_mail_dto() -> Mail:
    return Mail(to="hhssome@yandex.ru", subject="some_subject", message="some_message")


@pytest.fixture(scope="function")
def mock_invalid_mail_dto() -> Mail:
    return Mail(to="hhssome@yandex.ru", subject="", message="")


@pytest.fixture(scope="session")
def mock_mail_gateway() -> MailGatewayMock:
    return MailGatewayMock()


@pytest.fixture(scope="function")
def send_mail_service_with_mock(mock_mail_gateway) -> SendMailService:
    return SendMailService(mail_gateway=mock_mail_gateway)
