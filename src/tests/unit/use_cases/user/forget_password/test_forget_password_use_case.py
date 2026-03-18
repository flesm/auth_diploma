from src.app.application.use_cases.users.forget_password.use_case import (
    ForgetPasswordUseCase,
)
from src.app.application.use_cases.users.register.dto import (
    RegisterUserRequestDTO,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


async def test_forget_password_regular_user_success(
    forget_password_uc: ForgetPasswordUseCase,
    fake_uow: FakeSQLAUnitOfWork,
    register_regular_user_dto: RegisterUserRequestDTO,
) -> None:

    user = await fake_uow.users.create(register_regular_user_dto)

    result = await forget_password_uc(user.email)

    assert result == "Successfuly sent"
