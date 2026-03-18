from uuid import UUID

import pytest

from src.app.application.use_cases.roles.exceptions import (
    RoleNotFoundException,
)
from src.app.application.use_cases.roles.get.controllers import (
    GetAllRolesUseCase,
    GetRoleByIdUseCase,
)


async def test_get_role_by_id_success(
    get_role_by_id_uc: GetRoleByIdUseCase, role_id: UUID
) -> None:
    result = await get_role_by_id_uc(role_id=role_id)

    assert result.id == role_id


async def test_get_role_by_foreign_id_not_found(
    get_role_by_id_uc: GetRoleByIdUseCase, foreign_role_id: UUID
) -> None:
    with pytest.raises(RoleNotFoundException):
        await get_role_by_id_uc(role_id=foreign_role_id)


async def test_get_all_roles_success(
    get_all_roles_uc: GetAllRolesUseCase, role_id: UUID
) -> None:
    result = await get_all_roles_uc()

    assert result is not None
    assert len(result) == 1
