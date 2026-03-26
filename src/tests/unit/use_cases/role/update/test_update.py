from uuid import UUID

import pytest

from src.app.application.use_cases.roles.exceptions import (
    RoleAlreadyExistException,
    RoleNotFoundException,
)
from src.app.application.use_cases.roles.update.dto import UpdateRoleRequestDto
from src.app.application.use_cases.roles.update.use_case import (
    UpdateRoleUseCase,
)


class TestUpdate:

    async def test_case_1(
        self,
        update_role_uc: UpdateRoleUseCase,
        role_dto: UpdateRoleRequestDto,
        role_id: UUID,
    ) -> None:

            updated_role = await update_role_uc(role_id=role_id, dto=role_dto)

            assert updated_role.id == role_id
            assert updated_role.name == role_dto.name

    async def test_case_2(
        self,
        update_role_uc: UpdateRoleUseCase,
        role_dto: UpdateRoleRequestDto,
        foreign_role_id: UUID,
    ) -> None:
            with pytest.raises(RoleNotFoundException):
                await update_role_uc(role_id=foreign_role_id, dto=role_dto)

    async def test_case_3(
        self,
        update_role_uc: UpdateRoleUseCase,
        existing_role_dto: UpdateRoleRequestDto,
        another_role_id: UUID,
    ) -> None:
            with pytest.raises(RoleAlreadyExistException):
                await update_role_uc(role_id=another_role_id, dto=existing_role_dto)
