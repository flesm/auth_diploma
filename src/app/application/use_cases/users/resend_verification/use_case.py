from src.app.application.interfaces.email.email_sender import IEmailSender
from src.app.application.interfaces.jwt.jwt_encoder import IJwtTokenEncoder
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.users.exceptions import (
    UserAlreadyVerifiedException,
    UserNotFound,
)


class ResendVerificationEmailUseCase:
    def __init__(
        self,
        rdbms_uow: IUnitOfWork,
        jwt_encoder: IJwtTokenEncoder,
        email_sender: IEmailSender,
    ):
        self._rdbms_uow = rdbms_uow
        self._email_sender = email_sender
        self._jwt_encoder = jwt_encoder

    async def __call__(self, email: str) -> str:
        async with self._rdbms_uow():
            user = await self._rdbms_uow.users.get_by_email(email=email)
            if not user:
                raise UserNotFound("User not found")

            if user.is_verified:
                raise UserAlreadyVerifiedException("User already verified")

        token = self._jwt_encoder.encode_verify_token(email=email)

        await self._email_sender.send_verification_email(
            email=email, token=token
        )
        return "Verification email resent"
