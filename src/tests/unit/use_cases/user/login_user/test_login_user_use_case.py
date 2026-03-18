import pytest

from src.app.application.use_cases.users.auth.login.dto import LoginRequestDTO
from src.app.application.use_cases.users.auth.login.exceptions import (
    InvalidCredentialsException,
)
from src.app.application.use_cases.users.auth.login.use_case import (
    LoginUseCase,
)


async def test_login_regular_user_success(
    login_existed_user_dto: LoginRequestDTO,
    login_user_uc: LoginUseCase,
) -> None:
    result = await login_user_uc(dto=login_existed_user_dto)

    assert result.token_type == 'bearer'


async def test_login_foreign_user_not_found(
    login_foreign_user_dto: LoginRequestDTO,
    login_user_uc: LoginUseCase,
) -> None:
    with pytest.raises(InvalidCredentialsException):
        await login_user_uc(dto=login_foreign_user_dto)
