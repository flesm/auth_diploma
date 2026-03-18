from uuid import UUID

import pytest

from src.app.application.use_cases.permissions.exceptions import (
    PermissionNotFoundException,
)
from src.app.application.use_cases.permissions.get.use_case import (
    GetAllPermissionsUseCase,
    GetPermissionByIdUseCase,
)


async def test_get_permission_by_id_success(
    get_permission_by_id_uc: GetPermissionByIdUseCase, permission_id: UUID
) -> None:
    result = await get_permission_by_id_uc(permission_id=permission_id)

    assert result.id == permission_id


async def test_get_permission_by_foreign_id_not_found(
    get_permission_by_id_uc: GetPermissionByIdUseCase,
    foreign_permission_id: UUID,
) -> None:
    with pytest.raises(PermissionNotFoundException):
        await get_permission_by_id_uc(permission_id=foreign_permission_id)


async def test_get_all_permissions_success(
    get_all_permissions_uc: GetAllPermissionsUseCase, permission_id: UUID
) -> None:
    result = await get_all_permissions_uc()

    assert result is not None
    assert len(result) == 1
