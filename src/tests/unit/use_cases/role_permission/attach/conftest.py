import pytest

from src.app.application.use_cases.roles_permissions.attach.use_case import (
    AttachPermissionToRoleUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def attach_permission_to_role_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> AttachPermissionToRoleUseCase:
    return AttachPermissionToRoleUseCase(rdbms_uow=fake_uow)
