from fastapi import APIRouter, Depends

from src.business_logic.mail import dto
from src.business_logic.mail.services.send_mail import SendMailService
from src.presentation.api.di.stub import Stub

router = APIRouter(prefix="/mail", tags=["posts"])


@router.post("/")
async def send_message(
    mail_data: dto.Mail, service: SendMailService = Depends(Stub(SendMailService))
) -> dto.MailStatus:
    return await service(mail_data=mail_data)
