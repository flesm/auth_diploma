from src.app.application.interfaces.crypto.password_cryptografer import (
    IPasswordCryptografer,
)
from src.app.application.interfaces.jwt.jwt_encoder import IJwtTokenEncoder
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.users.auth.login.dto import (
    LoginRequestDTO,
    LoginResponseDTO,
)
from src.app.application.use_cases.users.auth.login.exceptions import (
    InvalidCredentialsException,
)


class LoginUseCase:
    def __init__(
        self,
        rdbms_uow: IUnitOfWork,
        jwt_encoder: IJwtTokenEncoder,
        password_cryptografer: IPasswordCryptografer,
    ):
        self._rdbms_uow = rdbms_uow
        self._jwt_encoder = jwt_encoder
        self._password_cryptografer = password_cryptografer

    async def __call__(self, dto: LoginRequestDTO) -> LoginResponseDTO:
        async with self._rdbms_uow():
            user = await self._rdbms_uow.users.get_by_email(dto.email)
            if not user or not self._password_cryptografer.verify(
                dto.password, user.hashed_password
            ):
                raise InvalidCredentialsException()

            is_staff = False
            role_name = None
            if user.role_id:
                role_obj = await self._rdbms_uow.roles.get_by_id(user.role_id)
                if role_obj:
                    role_name = role_obj.name
                    if role_obj.name in ("admin", "superadmin"):
                        is_staff = True

        access_token = self._jwt_encoder.encode_access_token(
            user_id=str(user.id),
            username=user.first_name,
            is_staff=is_staff,
            email=user.email,
            role=role_name or "intern",
        )
        refresh_token = self._jwt_encoder.encode_refresh_token(
            user_id=str(user.id)
        )

        return LoginResponseDTO(
            access_token=access_token, refresh_token=refresh_token
        )
