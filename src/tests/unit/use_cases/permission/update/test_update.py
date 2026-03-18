from uuid import UUID

import pytest

from src.app.application.use_cases.permissions.exceptions import (
    PermissionAlreadyExistException,
    PermissionNotFoundException,
)
from src.app.application.use_cases.permissions.update.dto import (
    UpdatePermissionRequestDto,
)
from src.app.application.use_cases.permissions.update.use_case import (
    UpdatePermissionUseCase,
)


async def test_update_permission_success(
    update_permission_uc: UpdatePermissionUseCase,
    permission_dto: UpdatePermissionRequestDto,
    permission_id: UUID,
) -> None:

    updated_permission = await update_permission_uc(
        permission_id=permission_id, dto=permission_dto
    )

    assert updated_permission.id == permission_id
    assert updated_permission.name == permission_dto.name


async def test_update_permission_not_found(
    update_permission_uc: UpdatePermissionUseCase,
    permission_dto: UpdatePermissionRequestDto,
    foreign_permission_id: UUID,
) -> None:
    with pytest.raises(PermissionNotFoundException):
        await update_permission_uc(
            permission_id=foreign_permission_id, dto=permission_dto
        )


async def test_update_permission_already_exists(
    update_permission_uc: UpdatePermissionUseCase,
    existing_permission_dto: UpdatePermissionRequestDto,
    another_permission_id: UUID,
) -> None:
    with pytest.raises(PermissionAlreadyExistException):
        await update_permission_uc(
            permission_id=another_permission_id, dto=existing_permission_dto
        )
