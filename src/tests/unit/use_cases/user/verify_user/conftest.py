import pytest

from src.app.application.use_cases.users.verify_email.use_cases import (
    VerifyUserUseCase,
)
from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def verify_user_uc(
    fake_uow: FakeSQLAUnitOfWork,
    fake_jwt_encoder: FakeJwtTokenEncoder,
) -> VerifyUserUseCase:
    return VerifyUserUseCase(
        rdbms_uow=fake_uow,
        jwt_encoder=fake_jwt_encoder,
    )
