import pytest

from src.app.application.use_cases.users.auth.login.use_case import LoginUseCase
from src.app.application.use_cases.users.auth.refresh.use_case import (
    RefreshTokenUseCase,
)
from src.app.application.use_cases.users.exceptions import (
    InvalidOrExpiredTokenException,
)
from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder


class TestRefreshTokenUseCase:

    async def test_case_1(
        self,
        login_existed_user_dto,
        login_user_uc: LoginUseCase,
        refresh_token_uc: RefreshTokenUseCase,
        fake_jwt_encoder: FakeJwtTokenEncoder,
    ) -> None:
            login_result = await login_user_uc(dto=login_existed_user_dto)

            refreshed_access_token = await refresh_token_uc(login_result.refresh_token)
            payload = fake_jwt_encoder.decode_access_token(refreshed_access_token)

            assert payload.get("email") == login_existed_user_dto.email
            assert payload.get("role") == "common"

    async def test_case_2(
        self,
        invalid_token: str,
        refresh_token_uc: RefreshTokenUseCase,
    ) -> None:
            with pytest.raises(InvalidOrExpiredTokenException):
                await refresh_token_uc(invalid_token)
