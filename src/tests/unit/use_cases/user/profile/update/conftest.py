import pytest

from src.app.application.use_cases.users.profile.update.use_case import (
    UpdateProfileUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def update_user_profile_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> UpdateProfileUseCase:
    return UpdateProfileUseCase(
        rdbms_uow=fake_uow,
    )


@pytest.fixture
def payload_for_update_common_user_profile() -> dict[str, str]:
    return {
        "first_name": "John",
        "last_name": "Bell",
        "role_id": "8fa85f64-5717-4562-b3fc-2c963f66afa6",
    }
