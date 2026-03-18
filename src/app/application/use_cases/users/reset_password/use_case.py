from src.app.application.interfaces.crypto.password_cryptografer import (
    IPasswordCryptografer,
)
from src.app.application.interfaces.email.email_sender import IEmailSender
from src.app.application.interfaces.jwt.jwt_encoder import IJwtTokenEncoder
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.users.exceptions import UserNotFound
from src.app.application.use_cases.users.reset_password.dto import (
    ResetPasswordRequestDTO,
)


class ResetPasswordUseCase:
    def __init__(
        self,
        rdbms_uow: IUnitOfWork,
        jwt_encoder: IJwtTokenEncoder,
        email_sender: IEmailSender,
        password_cryptografer: IPasswordCryptografer,
    ):
        self._rdbms_uow = rdbms_uow
        self._jwt_encoder = jwt_encoder
        self._email_sender = email_sender
        self._password_cryptografer = password_cryptografer

    async def __call__(self, dto: ResetPasswordRequestDTO) -> str:
        email = self._jwt_encoder.decode_reset_token(token=dto.token)

        async with self._rdbms_uow():
            user = await self._rdbms_uow.users.get_by_email(email=email)
            if not user:
                raise UserNotFound("User not found")

            new_hashed_pwd = self._password_cryptografer.hash(
                password=dto.new_password
            )
            await self._rdbms_uow.users.update_password(
                new_hashed_password=new_hashed_pwd, user=user
            )

        return "Password reset successful!"
