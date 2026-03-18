from src.app.application.interfaces.jwt.jwt_encoder import IJwtTokenEncoder
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.users.exceptions import (
    UserAlreadyVerifiedException,
    UserNotFound,
)
from src.app.config import Config


class VerifyUserUseCase:
    def __init__(
        self,
        rdbms_uow: IUnitOfWork,
        jwt_encoder: IJwtTokenEncoder,
        config: Config,
    ):
        self._rdbms_uow = rdbms_uow
        self._verify_secret_key = config.JWT.verify_email_secret_key
        self._jwt_encoder = jwt_encoder

    async def __call__(self, token: str) -> str:
        email = self._jwt_encoder.decode_verify_token(token=token)

        async with self._rdbms_uow():
            user = await self._rdbms_uow.users.get_by_email(email=email)
            if not user:
                raise UserNotFound("User not found")

            if user.is_verified:
                raise UserAlreadyVerifiedException("User already verified")

            await self._rdbms_uow.users.mark_as_verified(user=user)
            return "User successfully verified"
