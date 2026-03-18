from uuid import UUID

import pytest

from src.app.application.use_cases.roles_permissions.detach.use_case import (
    DetachRoleWithPermissionUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def detach_role_with_permission_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> DetachRoleWithPermissionUseCase:
    return DetachRoleWithPermissionUseCase(rdbms_uow=fake_uow)


@pytest.fixture
def attached_role_with_permission(
    role_id: UUID, permission_id: UUID, fake_uow: FakeSQLAUnitOfWork
) -> None:
    fake_uow.roles_permissions.role_permissions.add((role_id, permission_id))
