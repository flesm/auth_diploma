import pytest

from src.app.application.use_cases.roles.delete.controllers import (
    DeleteRoleUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def delete_role_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> DeleteRoleUseCase:
    return DeleteRoleUseCase(rdbms_uow=fake_uow)
