from abc import ABC, abstractmethod


class IEmailSender(ABC):

    @abstractmethod
    async def send_reset_password_email(self, email: str, token: str) -> None:
        pass

    @abstractmethod
    async def send_verification_email(self, email: str, token: str) -> None:
        pass
