import pytest
from jose import ExpiredSignatureError

from src.app.application.use_cases.users.auth.get_current_user.use_case import (  # noqa
    GetCurrentUserUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


class TestGetCurrentUserUseCase:

    async def test_case_1(
        self,
        fake_uow: FakeSQLAUnitOfWork,
        access_token_of_regular_user: str,
        get_current_user_uc: GetCurrentUserUseCase,
    ) -> None:
            result = await get_current_user_uc(token=access_token_of_regular_user)
            assert result.id in [user.id for user in fake_uow.users.users]

    async def test_case_2(
        self,
        fake_uow: FakeSQLAUnitOfWork,
        expired_token: str,
        get_current_user_uc: GetCurrentUserUseCase,
    ) -> None:
            with pytest.raises(ExpiredSignatureError):
                await get_current_user_uc(token=expired_token)
