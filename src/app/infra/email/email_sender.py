from fastapi import BackgroundTasks
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType

from src.app.application.interfaces.email.email_sender import IEmailSender
from src.app.config import Config


class FMEmailSender(IEmailSender):
    def __init__(self, config: Config, mail_config: ConnectionConfig) -> None:
        self._fm = FastMail(mail_config)
        self._app_host = config.APP.host
        self._expire_minutes = config.JWT.expire_minutes
        self._background_tasks: BackgroundTasks = BackgroundTasks()

    async def send_reset_password_email(self, email: str, token: str) -> None:

        reset_url = f"{self._app_host}/reset/{token}"

        email_body = {
            "link_expiry_min": self._expire_minutes,
            "link": reset_url,
        }

        message = MessageSchema(
            subject="Password Reset Instructions",
            recipients=[email],
            template_body=email_body,
            subtype=MessageType.html,
        )
        await self._fm.send_message(
            message, template_name="mail/password_reset.html"
        )

    async def send_verification_email(self, email: str, token: str) -> None:
        verify_url = f"{self._app_host}" f"/verify_email/{token}"

        email_body = {
            "link_expiry_min": self._expire_minutes,
            "link": verify_url,
        }

        message = MessageSchema(
            subject="Verify Your Email",
            recipients=[email],
            template_body=email_body,
            subtype=MessageType.html,
        )
        await self._fm.send_message(
            message, template_name="mail/verify_email.html"
        )
