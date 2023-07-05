import pytest

from src.business_logic.mail.utils import _validate_email


@pytest.mark.asyncio
async def test_success_validate_email(success_emails):
    result = []

    for email in success_emails:
        result.append(_validate_email(email=email))

    assert all(result) is True


@pytest.mark.asyncio
async def test_invalid_validate_email(invalid_emails):
    result = []

    for email in invalid_emails:
        result.append(_validate_email(email=email))

    assert all(result) is False
