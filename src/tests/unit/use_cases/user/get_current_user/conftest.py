import pytest

from src.app.application.use_cases.users.auth.get_current_user.use_case import (  # noqa
    GetCurrentUserUseCase,
)
from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def get_current_user_uc(
    fake_uow: FakeSQLAUnitOfWork,
    fake_jwt_encoder: FakeJwtTokenEncoder,
) -> GetCurrentUserUseCase:
    return GetCurrentUserUseCase(
        rdbms_uow=fake_uow,
        jwt_encoder=fake_jwt_encoder,
    )


@pytest.fixture
def expired_token() -> str:
    return (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        "eyJzdWIiOiI4NzRhZTg3My1mMGE3LTQ1NzEtYW"
        "JkOS1mYjc4NzIzZGUxOTAiLCJleHAiOjE3NTQ5MDU2Mzh9."
        "XOjckzU5YCdWBMxfu8-6PQC4JBm4B1kjb0-wYRQIf_Y"
    )
