from unittest.mock import patch

import pytest

from src.presentation.api.settings.config import load_config
from tests.mocks import ConfigExtractorMock


@pytest.mark.asyncio
async def test_load_config():
    with patch(
        "src.presentation.api.settings.config.ConfigExtractor", ConfigExtractorMock
    ):
        config = load_config()

        assert config.mail.port == ConfigExtractorMock.mail_port
        assert config.mail.host == ConfigExtractorMock.mail_host
        assert config.mail.password == ConfigExtractorMock.mail_password
        assert config.mail.username == ConfigExtractorMock.mail_username
