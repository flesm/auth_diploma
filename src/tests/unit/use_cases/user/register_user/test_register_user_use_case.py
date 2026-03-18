import pytest

from src.app.application.use_cases.users.register.dto import (
    RegisterUserRequestDTO,
)
from src.app.application.use_cases.users.register.exceptions import (
    EmailAlreadyRegisteredException,
)
from src.app.application.use_cases.users.register.use_case import (
    RegisterUserUseCase,
)
from src.tests.environment.email.email_sender import FakeFMEmailSender
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


async def test_register_regular_user_success(
    register_regular_user_dto: RegisterUserRequestDTO,
    register_user_uc: RegisterUserUseCase,
    fake_uow: FakeSQLAUnitOfWork,
    fake_email_sender: FakeFMEmailSender,
) -> None:
    result = await register_user_uc.create_user(dto=register_regular_user_dto)

    assert result.email == register_regular_user_dto.email
    assert len(fake_uow.users._users) == 1

    await register_user_uc.send_verification_email(
        email=register_regular_user_dto.email
    )

    assert len(fake_email_sender.sent_emails) == 1

    email_type, email, token = fake_email_sender.sent_emails[0]
    assert email_type == 'verify'
    assert email == register_regular_user_dto.email


async def test_register_regular_user_email_already_registered_success(
    register_regular_user_dto: RegisterUserRequestDTO,
    register_user_uc: RegisterUserUseCase,
    fake_uow: FakeSQLAUnitOfWork,
    fake_email_sender: FakeFMEmailSender,
) -> None:
    await register_user_uc.create_user(dto=register_regular_user_dto)

    with pytest.raises(EmailAlreadyRegisteredException):
        await register_user_uc.create_user(dto=register_regular_user_dto)

    assert len(fake_uow.users._users) == 1
