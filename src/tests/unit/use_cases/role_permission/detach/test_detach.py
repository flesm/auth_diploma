from uuid import UUID

import pytest

from src.app.application.use_cases.permissions.exceptions import (
    PermissionNotFoundException,
)
from src.app.application.use_cases.roles.exceptions import (
    RoleNotFoundException,
)
from src.app.application.use_cases.roles_permissions.detach.use_case import (
    DetachRoleWithPermissionUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


async def test_detach_success(
    detach_role_with_permission_uc: DetachRoleWithPermissionUseCase,
    role_id: UUID,
    permission_id: UUID,
    fake_uow: FakeSQLAUnitOfWork,
    attached_role_with_permission: None,
) -> None:
    assert len(fake_uow.roles_permissions.role_permissions) == 1

    await detach_role_with_permission_uc(
        role_id=role_id, permission_id=permission_id
    )

    assert (
        role_id,
        permission_id,
    ) not in fake_uow.roles_permissions.role_permissions
    assert len(fake_uow.roles_permissions.role_permissions) == 0


async def test_detach_role_not_found(
    detach_role_with_permission_uc: DetachRoleWithPermissionUseCase,
    foreign_role_id: UUID,
    permission_id: UUID,
    fake_uow: FakeSQLAUnitOfWork,
    attached_role_with_permission: None,
) -> None:
    assert len(fake_uow.roles_permissions.role_permissions) == 1

    with pytest.raises(RoleNotFoundException):
        await detach_role_with_permission_uc(
            role_id=foreign_role_id, permission_id=permission_id
        )

    assert len(fake_uow.roles_permissions.role_permissions) == 1


async def test_detach_permission_not_found(
    detach_role_with_permission_uc: DetachRoleWithPermissionUseCase,
    role_id: UUID,
    foreign_permission_id: UUID,
    fake_uow: FakeSQLAUnitOfWork,
    attached_role_with_permission: None,
) -> None:
    assert len(fake_uow.roles_permissions.role_permissions) == 1

    with pytest.raises(PermissionNotFoundException):
        await detach_role_with_permission_uc(
            role_id=role_id, permission_id=foreign_permission_id
        )

    assert len(fake_uow.roles_permissions.role_permissions) == 1
