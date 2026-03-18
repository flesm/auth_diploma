from jose import ExpiredSignatureError, JWTError

from src.app.application.interfaces.jwt.jwt_encoder import IJwtTokenEncoder
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.users.exceptions import (
    InvalidOrExpiredTokenException,
    UserAlreadyVerifiedException,
    UserNotFound,
)


class VerifyUserUseCase:
    def __init__(
        self,
        rdbms_uow: IUnitOfWork,
        jwt_encoder: IJwtTokenEncoder,
    ):
        self._rdbms_uow = rdbms_uow
        self._jwt_encoder = jwt_encoder

    async def __call__(self, token: str) -> str:
        try:
            email = self._jwt_encoder.decode_verify_token(token=token)
        except (ExpiredSignatureError, JWTError):
            raise InvalidOrExpiredTokenException(
                "Invalid or expired verification token."
            )

        async with self._rdbms_uow():
            user = await self._rdbms_uow.users.get_by_email(email=email)
            if not user:
                raise UserNotFound("User not found")

            if user.is_verified:
                raise UserAlreadyVerifiedException("User already verified")

            await self._rdbms_uow.users.mark_as_verified(user=user)
            return "User successfully verified"
