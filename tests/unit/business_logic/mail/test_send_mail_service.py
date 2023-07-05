import pytest

from src.business_logic.mail.enum import Status


@pytest.mark.asyncio
async def test_valid_send_mail_service(
    send_mail_service_with_mock, mock_success_mail_dto
):
    data = await send_mail_service_with_mock(mail_data=mock_success_mail_dto)

    assert data.status == Status.SUCCESS


@pytest.mark.asyncio
async def test_invalid_send_mail_service(
    send_mail_service_with_mock, mock_invalid_mail_dto
):
    data = await send_mail_service_with_mock(mail_data=mock_invalid_mail_dto)

    assert data.status == Status.DENIED
