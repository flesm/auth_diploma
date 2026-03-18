import pytest

from src.app.application.use_cases.permissions.get.use_case import (
    GetPermissionByIdUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def get_permission_by_id_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> GetPermissionByIdUseCase:
    return GetPermissionByIdUseCase(rdbms_uow=fake_uow)
