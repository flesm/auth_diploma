from uuid import UUID

from src.app.application.interfaces.jwt.jwt_encoder import IJwtTokenEncoder
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.users.exceptions import (
    InvalidOrExpiredTokenException,
    UserNotFound,
)


class RefreshTokenUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork, jwt_encoder: IJwtTokenEncoder):
        self._jwt_encoder = jwt_encoder
        self._rdbms_uow = rdbms_uow

    async def __call__(self, refresh_token: str) -> str:
        user_id = self._jwt_encoder.decode_refresh_token(token=refresh_token)
        if not user_id:
            raise InvalidOrExpiredTokenException()

        async with self._rdbms_uow():
            user = await self._rdbms_uow.users.get_by_id(user_id=UUID(user_id))
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

        return self._jwt_encoder.encode_access_token(
            user_id=user_id,
            username=user.first_name,
            is_staff=is_staff,
            email=user.email,
            role=role_name or "intern",
        )
