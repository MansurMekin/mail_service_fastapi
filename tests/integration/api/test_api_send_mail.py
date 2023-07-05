import pytest


class TestMailControllers:
    @pytest.mark.asyncio
    async def test_send_message_controller(self, client, mock_success_mail_dto):
        test_data = {
            "to": mock_success_mail_dto.to,
            "subject": mock_success_mail_dto.subject,
            "message": mock_success_mail_dto.message,
        }
        response = await client.post("mail/", json=test_data)

        assert response.json() == {"status": "success"}

    @pytest.mark.asyncio
    async def test_invalid_send_message_controller(self, client, mock_invalid_mail_dto):
        test_data = {
            "to": mock_invalid_mail_dto.to,
            "subject": mock_invalid_mail_dto.subject,
            "message": mock_invalid_mail_dto.message,
        }

        response = await client.post("mail/", json=test_data)

        assert response.json() == {"status": "denied"}
