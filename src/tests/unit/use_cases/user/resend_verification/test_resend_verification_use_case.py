import pytest

from src.app.application.use_cases.users.exceptions import (
    UserAlreadyVerifiedException,
    UserNotFound,
)
from src.app.application.use_cases.users.register.dto import (
    RegisterUserRequestDTO,
)
from src.app.application.use_cases.users.resend_verification.use_case import (
    ResendVerificationEmailUseCase,
)
from src.tests.environment.email.email_sender import FakeFMEmailSender
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


class TestResendVerificationUseCase:

    async def test_case_1(
        self,
        resend_verification_uc: ResendVerificationEmailUseCase,
        non_existent_email: str,
    ) -> None:
            with pytest.raises(UserNotFound):
                await resend_verification_uc(non_existent_email)

    async def test_case_2(
        self,
        resend_verification_uc: ResendVerificationEmailUseCase,
        fake_uow: FakeSQLAUnitOfWork,
        fake_email_sender: FakeFMEmailSender,
        register_regular_user_dto: RegisterUserRequestDTO,
    ) -> None:

            user = await fake_uow.users.create(dto=register_regular_user_dto)
            user.is_verified = True

            with pytest.raises(UserAlreadyVerifiedException):
                await resend_verification_uc(user.email)

            assert len(fake_email_sender.sent_emails) == 0

    async def test_case_3(
        self,
        register_regular_user_dto: RegisterUserRequestDTO,
        resend_verification_uc: ResendVerificationEmailUseCase,
        fake_uow: FakeSQLAUnitOfWork,
        fake_email_sender: FakeFMEmailSender,
    ) -> None:
            user = await fake_uow.users.create(dto=register_regular_user_dto)

            result = await resend_verification_uc(user.email)

            assert result == "Verification email resent"
            assert len(fake_email_sender.sent_emails) == 1

            email_type, email, token = fake_email_sender.sent_emails[0]
            assert email_type == "verify"
            assert email == user.email
