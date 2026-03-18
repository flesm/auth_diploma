from src.app.application.entities.user import UserEntity
from src.app.application.interfaces.crypto.password_cryptografer import (
    IPasswordCryptografer,
)
from src.app.application.interfaces.email.email_sender import IEmailSender
from src.app.application.interfaces.jwt.jwt_encoder import IJwtTokenEncoder
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.users.register.dto import (
    RegisterUserRequestDTO,
)
from src.app.application.use_cases.users.register.exceptions import (
    EmailAlreadyRegisteredException,
)


class RegisterUserUseCase:
    def __init__(
        self,
        rdbms_uow: IUnitOfWork,
        email_sender: IEmailSender,
        jwt_encoder: IJwtTokenEncoder,
        password_cryptografer: IPasswordCryptografer,
    ) -> None:
        self._rdbms_uow = rdbms_uow
        self._email_sender = email_sender
        self._jwt_encoder = jwt_encoder
        self._password_cryptografer = password_cryptografer

    async def create_user(self, dto: RegisterUserRequestDTO) -> UserEntity:
        async with self._rdbms_uow():
            existing = await self._rdbms_uow.users.get_by_email(
                email=dto.email
            )
            if existing:
                raise EmailAlreadyRegisteredException()

            dto.hashed_password = self._password_cryptografer.hash(
                dto.hashed_password
            )
            user = await self._rdbms_uow.users.create(dto=dto)

        return user

    async def send_verification_email(self, email: str) -> None:
        token = self._jwt_encoder.encode_verify_token(email=email)
        await self._email_sender.send_verification_email(
            email=email, token=token
        )
