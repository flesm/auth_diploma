import pytest
from faker import Faker

from src.app.application.use_cases.users.register.dto import (
    RegisterUserRequestDTO,
)
from src.app.application.use_cases.users.reset_password.dto import (
    ResetPasswordRequestDTO,
)
from src.app.application.use_cases.users.reset_password.use_case import (
    ResetPasswordUseCase,
)
from src.tests.environment.crypto.password_cryptografer import (
    FakePasswordCryptografer,
)
from src.tests.environment.email.email_sender import FakeFMEmailSender
from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def reset_password_uc(
    fake_uow: FakeSQLAUnitOfWork,
    fake_email_sender: FakeFMEmailSender,
    fake_jwt_encoder: FakeJwtTokenEncoder,
    fake_password_cryptografer: FakePasswordCryptografer,
) -> ResetPasswordUseCase:
    return ResetPasswordUseCase(
        rdbms_uow=fake_uow,
        email_sender=fake_email_sender,
        jwt_encoder=fake_jwt_encoder,
        password_cryptografer=fake_password_cryptografer,
    )


@pytest.fixture
def reset_password_regular_user_dto(
    faker: Faker,
    fake_jwt_encoder: FakeJwtTokenEncoder,
    register_regular_user_dto: RegisterUserRequestDTO,
) -> ResetPasswordRequestDTO:
    token = fake_jwt_encoder.encode_reset_token(
        email=register_regular_user_dto.email
    )
    return ResetPasswordRequestDTO(token=token, new_password=faker.password())
