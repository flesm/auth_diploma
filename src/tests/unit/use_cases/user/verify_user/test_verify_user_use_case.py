import pytest

from src.app.application.use_cases.users.exceptions import (
    InvalidOrExpiredTokenException,
    UserAlreadyVerifiedException,
    UserNotFound,
)
from src.app.application.use_cases.users.register.dto import (
    RegisterUserRequestDTO,
)
from src.app.application.use_cases.users.verify_email.use_cases import (
    VerifyUserUseCase,
)
from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


class TestVerifyUserUseCase:

    async def test_case_1(
        self,
        register_regular_user_dto: RegisterUserRequestDTO,
        verify_user_uc: VerifyUserUseCase,
        fake_uow: FakeSQLAUnitOfWork,
        fake_jwt_encoder: FakeJwtTokenEncoder,
    ) -> None:
            user = await fake_uow.users.create(dto=register_regular_user_dto)
            token = fake_jwt_encoder.encode_verify_token(email=user.email)

            result = await verify_user_uc(token=token)

            assert result == "User successfully verified"
            assert user.is_verified is True

    async def test_case_2(
        self,
        register_regular_user_dto: RegisterUserRequestDTO,
        verify_user_uc: VerifyUserUseCase,
        fake_uow: FakeSQLAUnitOfWork,
        fake_jwt_encoder: FakeJwtTokenEncoder,
    ) -> None:

            user = await fake_uow.users.create(dto=register_regular_user_dto)
            user.is_verified = True
            token = fake_jwt_encoder.encode_verify_token(email=user.email)

            with pytest.raises(UserAlreadyVerifiedException):
                await verify_user_uc(token=token)

    async def test_case_3(
        self,
        verify_user_uc: VerifyUserUseCase,
        fake_jwt_encoder: FakeJwtTokenEncoder,
        invalid_token: str,
    ) -> None:

            with pytest.raises(InvalidOrExpiredTokenException):
                await verify_user_uc(token=invalid_token)

    async def test_case_4(
        self,
        verify_user_uc: VerifyUserUseCase,
        fake_jwt_encoder: FakeJwtTokenEncoder,
        non_existent_email: str,
    ) -> None:

            token = fake_jwt_encoder.encode_verify_token(email=non_existent_email)

            with pytest.raises(UserNotFound):
                await verify_user_uc(token=token)
