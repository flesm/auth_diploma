import pytest

from src.app.application.use_cases.users.forget_password.use_case import (
    ForgetPasswordUseCase,
)
from src.tests.environment.email.email_sender import FakeFMEmailSender
from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def forget_password_uc(
    fake_uow: FakeSQLAUnitOfWork,
    fake_email_sender: FakeFMEmailSender,
    fake_jwt_encoder: FakeJwtTokenEncoder,
) -> ForgetPasswordUseCase:
    return ForgetPasswordUseCase(
        rdbms_uow=fake_uow,
        email_sender=fake_email_sender,
        jwt_encoder=fake_jwt_encoder,
    )
