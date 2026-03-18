from src.app.application.interfaces.email.email_sender import IEmailSender


class FakeFMEmailSender(IEmailSender):
    def __init__(self) -> None:
        self.sent_emails: list[tuple[str, str, str]] = []

    async def send_reset_password_email(self, email: str, token: str) -> None:
        self.sent_emails.append(('reset', email, token))

    async def send_verification_email(self, email: str, token: str) -> None:
        self.sent_emails.append(('verify', email, token))
