import pytest

from src.app.application.use_cases.permissions.delete.use_case import (
    DeletePermissionUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def delete_permission_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> DeletePermissionUseCase:
    return DeletePermissionUseCase(rdbms_uow=fake_uow)
