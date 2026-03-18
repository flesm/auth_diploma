import pytest

from src.app.application.use_cases.users.register.use_case import (
    RegisterUserUseCase,
)
from src.tests.environment.crypto.password_cryptografer import (
    FakePasswordCryptografer,
)
from src.tests.environment.email.email_sender import FakeFMEmailSender
from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def register_user_uc(
    fake_uow: FakeSQLAUnitOfWork,
    fake_email_sender: FakeFMEmailSender,
    fake_jwt_encoder: FakeJwtTokenEncoder,
    fake_password_cryptografer: FakePasswordCryptografer,
) -> RegisterUserUseCase:
    return RegisterUserUseCase(
        rdbms_uow=fake_uow,
        email_sender=fake_email_sender,
        jwt_encoder=fake_jwt_encoder,
        password_cryptografer=fake_password_cryptografer,
    )
