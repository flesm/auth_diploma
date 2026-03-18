from src.app.application.interfaces.email.email_sender import IEmailSender
from src.app.application.interfaces.jwt.jwt_encoder import IJwtTokenEncoder
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork


class ForgetPasswordUseCase:
    def __init__(
        self,
        rdbms_uow: IUnitOfWork,
        jwt_encoder: IJwtTokenEncoder,
        email_sender: IEmailSender,
    ):
        self._rdbms_uow = rdbms_uow
        self._jwt_encoder = jwt_encoder
        self._email_sender = email_sender

    async def __call__(self, email: str) -> str:
        token = self._jwt_encoder.encode_reset_token(email=email)
        await self._email_sender.send_reset_password_email(
            email=email, token=token
        )

        return "Successfuly sent"
