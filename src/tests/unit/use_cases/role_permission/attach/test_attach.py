from uuid import UUID

import pytest

from src.app.application.use_cases.permissions.exceptions import (
    PermissionNotFoundException,
)
from src.app.application.use_cases.roles.exceptions import (
    RoleNotFoundException,
)
from src.app.application.use_cases.roles_permissions.attach.use_case import (
    AttachPermissionToRoleUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


async def test_attach_success(
    attach_permission_to_role_uc: AttachPermissionToRoleUseCase,
    role_id: UUID,
    permission_id: UUID,
    fake_uow: FakeSQLAUnitOfWork,
) -> None:
    await attach_permission_to_role_uc(
        role_id=role_id, permission_id=permission_id
    )

    assert (
        role_id,
        permission_id,
    ) in fake_uow.roles_permissions.role_permissions


async def test_attach_role_not_found(
    attach_permission_to_role_uc: AttachPermissionToRoleUseCase,
    foreign_role_id: UUID,
    permission_id: UUID,
) -> None:
    with pytest.raises(RoleNotFoundException):
        await attach_permission_to_role_uc(
            role_id=foreign_role_id, permission_id=permission_id
        )


async def test_attach_permission_not_found(
    attach_permission_to_role_uc: AttachPermissionToRoleUseCase,
    role_id: UUID,
    foreign_permission_id: UUID,
) -> None:
    with pytest.raises(PermissionNotFoundException):
        await attach_permission_to_role_uc(
            role_id=role_id, permission_id=foreign_permission_id
        )


async def test_attach_already_exists(
    attach_permission_to_role_uc: AttachPermissionToRoleUseCase,
    role_id: UUID,
    permission_id: UUID,
    fake_uow: FakeSQLAUnitOfWork,
) -> None:
    await attach_permission_to_role_uc(
        role_id=role_id, permission_id=permission_id
    )

    await attach_permission_to_role_uc(
        role_id=role_id, permission_id=permission_id
    )

    assert len(fake_uow.roles_permissions.role_permissions) == 1
