from uuid import UUID

from src.app.application.interfaces.jwt.jwt_encoder import IJwtTokenEncoder
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.users.auth.get_current_user.dto import (
    CurrentUserResponseDto,
)
from src.app.application.use_cases.users.exceptions import (
    InvalidOrExpiredTokenException,
    UserNotFound,
)


class GetCurrentUserUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork, jwt_encoder: IJwtTokenEncoder):
        self._rdbms_uow = rdbms_uow
        self._jwt_encoder = jwt_encoder

    async def __call__(self, token: str) -> CurrentUserResponseDto:
        user_from_token = self._jwt_encoder.decode_access_token(token=token)
        if not user_from_token:
            raise InvalidOrExpiredTokenException()

        async with self._rdbms_uow():
            user = await self._rdbms_uow.users.get_by_id(
                user_id=UUID(user_from_token.get("user_id"))
            )
            if not user:
                raise UserNotFound()

            is_staff = False
            role_name = None
            if user.role_id:
                role_obj = await self._rdbms_uow.roles.get_by_id(user.role_id)
                if role_obj:
                    role_name = role_obj.name
                    if role_obj.name in ("admin", "superadmin"):
                        is_staff = True

        return CurrentUserResponseDto(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            is_active=user.is_active,
            is_verified=user.is_verified,
            is_staff=is_staff,
            role=role_name or user_from_token.get("role"),
        )
