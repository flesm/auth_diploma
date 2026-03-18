import pytest

from src.app.application.use_cases.users.resend_verification.use_case import (
    ResendVerificationEmailUseCase,
)
from src.tests.environment.email.email_sender import FakeFMEmailSender
from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def resend_verification_uc(
    fake_uow: FakeSQLAUnitOfWork,
    fake_email_sender: FakeFMEmailSender,
    fake_jwt_encoder: FakeJwtTokenEncoder,
) -> ResendVerificationEmailUseCase:
    return ResendVerificationEmailUseCase(
        rdbms_uow=fake_uow,
        email_sender=fake_email_sender,
        jwt_encoder=fake_jwt_encoder,
    )
