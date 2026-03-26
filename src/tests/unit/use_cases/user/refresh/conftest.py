import pytest

from src.app.application.use_cases.users.auth.refresh.use_case import (
    RefreshTokenUseCase,
)
from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def refresh_token_uc(
    fake_uow: FakeSQLAUnitOfWork,
    fake_jwt_encoder: FakeJwtTokenEncoder,
) -> RefreshTokenUseCase:
    return RefreshTokenUseCase(
        rdbms_uow=fake_uow,
        jwt_encoder=fake_jwt_encoder,
    )
