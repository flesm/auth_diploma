import pytest

from src.app.application.use_cases.permissions.create.dto import (
    CreatePermissionRequestDto,
)
from src.app.application.use_cases.permissions.create.use_case import (
    CreatePermissionUseCase,
)
from src.app.application.use_cases.permissions.exceptions import (
    PermissionAlreadyExistException,
)


async def test_create_permission_success(
    create_permission_uc: CreatePermissionUseCase,
    permission_dto: CreatePermissionRequestDto,
) -> None:
    result = await create_permission_uc(dto=permission_dto)

    assert result.name == permission_dto.name
    assert result.description == permission_dto.description


async def test_create_permission_already_exist(
    create_permission_uc: CreatePermissionUseCase,
    existed_permission_dto: CreatePermissionRequestDto,
) -> None:
    with pytest.raises(PermissionAlreadyExistException):
        await create_permission_uc(dto=existed_permission_dto)
