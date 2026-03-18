import pytest

from src.app.application.use_cases.permissions.get.use_case import (
    GetAllPermissionsUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def get_all_permissions_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> GetAllPermissionsUseCase:
    return GetAllPermissionsUseCase(rdbms_uow=fake_uow)
