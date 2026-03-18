import pytest

from src.app.application.use_cases.roles.create.dto import CreateRoleRequestDto
from src.app.application.use_cases.roles.create.use_case import (
    CreateRoleUseCase,
)
from src.app.application.use_cases.roles.exceptions import (
    RoleAlreadyExistException,
)


async def test_create_role_success(
    create_role_uc: CreateRoleUseCase, role_dto: CreateRoleRequestDto
) -> None:
    result = await create_role_uc(dto=role_dto)

    assert result.name == role_dto.name
    assert result.description == role_dto.description


async def test_create_role_already_exist(
    create_role_uc: CreateRoleUseCase, existed_role_dto: CreateRoleRequestDto
) -> None:
    with pytest.raises(RoleAlreadyExistException):
        await create_role_uc(dto=existed_role_dto)
