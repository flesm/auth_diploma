import pytest

from src.app.application.use_cases.users.profile.delete.use_case import (
    DeleteProfileUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def delete_user_profile_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> DeleteProfileUseCase:
    return DeleteProfileUseCase(
        rdbms_uow=fake_uow,
    )
