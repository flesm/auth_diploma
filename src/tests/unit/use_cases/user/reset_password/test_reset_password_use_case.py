import pytest
from faker import Faker

from src.app.application.use_cases.users.exceptions import UserNotFound
from src.app.application.use_cases.users.register.dto import (
    RegisterUserRequestDTO,
)
from src.app.application.use_cases.users.reset_password.dto import (
    ResetPasswordRequestDTO,
)
from src.app.application.use_cases.users.reset_password.use_case import (
    ResetPasswordUseCase,
)
from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


async def test_reset_password_regular_user_success(
    register_regular_user_dto: RegisterUserRequestDTO,
    reset_password_regular_user_dto: ResetPasswordRequestDTO,
    reset_password_uc: ResetPasswordUseCase,
    fake_uow: FakeSQLAUnitOfWork,
    fake_jwt_encoder: FakeJwtTokenEncoder,
) -> None:

    user = await fake_uow.users.create(dto=register_regular_user_dto)

    result = await reset_password_uc(dto=reset_password_regular_user_dto)

    assert result == "Password reset successful!"
    assert user.email == fake_jwt_encoder.decode_reset_token(
        reset_password_regular_user_dto.token
    )


async def test_reset_password_user_not_found(
    reset_password_regular_user_dto: ResetPasswordRequestDTO,
    reset_password_uc: ResetPasswordUseCase,
) -> None:

    with pytest.raises(UserNotFound):
        await reset_password_uc(reset_password_regular_user_dto)


@pytest.fixture
def reset_password_invalid_token_dto(
    faker: Faker,
) -> ResetPasswordRequestDTO:
    return ResetPasswordRequestDTO(
        token="token", new_password=faker.password()
    )
